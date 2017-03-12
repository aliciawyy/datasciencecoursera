"""
classifiers
"""
import numpy as np
from sklearn import naive_bayes
from sklearn.utils import multiclass


class GaussianNB(naive_bayes.GaussianNB):
    def _partial_fit(self, X, y, classes=None, _refit=False,
                     sample_weight=None):

        """
        Adapt the class with the same name in scikit-learn to accept missing 
        data in the given X and y.
        """
        # If the ratio of data variance between dimensions is too small, it
        # will cause numerical errors. To address this, we artificially
        # boost the variance by epsilon, a small fraction of the standard
        # deviation of the largest dimension.
        epsilon = 1e-9 * np.var(X, axis=0).max()

        if _refit:
            self.classes_ = None

        if getattr(self, 'classes_', None) is None:
            self.classes_ = multiclass.unique_labels(classes)
            # This is the first call to partial_fit:
            # initialize various cumulative counters
            n_features = X.shape[1]
            n_classes = len(self.classes_)
            self.theta_ = np.zeros((n_classes, n_features))
            self.sigma_ = np.zeros((n_classes, n_features))

            self.class_count_ = np.zeros((n_classes, n_features),
                                         dtype=np.int64)
            self.class_prior_ = np.zeros(n_classes, dtype=np.float64)

            # Initialise the class prior
            n_classes = len(self.classes_)
            # Take into account the priors
            if self.priors is not None:
                priors = np.asarray(self.priors)
                # Check that the provide prior match the number of classes
                if len(priors) != n_classes:
                    raise ValueError('Number of priors must match number of'
                                     ' classes.')
                # Check that the sum is 1
                if priors.sum() != 1.0:
                    raise ValueError('The sum of the priors should be 1.')
                # Check that the prior are non-negative
                if (priors < 0).any():
                    raise ValueError('Priors must be non-negative.')
                self.class_prior_ = priors
            else:
                # Initialize the priors to zeros for each class
                self.class_prior_ = np.zeros(len(self.classes_),
                                             dtype=np.float64)
        else:
            if X.shape[1] != self.theta_.shape[1]:
                msg = "Number of features %d does not match previous data %d."
                raise ValueError(msg % (X.shape[1], self.theta_.shape[1]))
            # Put epsilon back in each time
            self.sigma_[:, :] -= epsilon

        classes = self.classes_

        unique_y = np.unique(y)
        unique_y_in_classes = naive_bayes.in1d(unique_y, classes)

        if not np.all(unique_y_in_classes):
            raise ValueError("The target label(s) %s in y do not exist in the "
                             "initial classes %s" %
                             (unique_y[~unique_y_in_classes], classes))

        class_prior = np.zeros(len(self.classes_), dtype=np.float64)
        for y_i in unique_y:
            i = classes.searchsorted(y_i)
            class_prior[i] = np.sum(y == y_i)
            X_i = X[y == y_i]

            if sample_weight is not None:
                sw_i = sample_weight[y == y_i]
                N_i = sw_i.sum()
            else:
                sw_i = None
                N_i = np.sum(~np.isnan(X_i), axis=0)

            new_theta, new_sigma = update_mean_variance(
                self.class_count_[i], self.theta_[i], self.sigma_[i],
                X_i, sw_i)

            new_theta[np.isnan(new_theta)] = 0.
            new_sigma[np.isnan(new_sigma)] = 0.

            self.theta_[i, :] = new_theta
            self.sigma_[i, :] = new_sigma
            self.class_count_[i] += N_i

        self.sigma_[:, :] += epsilon

        # Update if only no priors is provided
        if self.priors is None:
            # Empirical prior, with sample_weight taken into account
            self.class_prior_ += class_prior

        return self

    def _joint_log_likelihood(self, X):
        naive_bayes.check_is_fitted(self, "classes_")

        class_prior = np.log(self.class_prior_ / np.sum(self.class_prior_))
        n_ij_sigma = np.log(2. * np.pi * self.sigma_)
        joint_log_likelihood = []
        for i in range(np.size(self.classes_)):
            n_ij = -0.5 * np.sum(((X - self.theta_[i]) ** 2) / self.sigma_[i] + n_ij_sigma[i], 1)
            joint_log_likelihood.append(class_prior[i] + n_ij)

        joint_log_likelihood = np.array(joint_log_likelihood).T
        return joint_log_likelihood


def update_mean_variance(n_past, mu, var, X, sample_weight=None):
    if X.shape[0] == 0:
        return mu, var

    # Compute (potentially weighted) mean and variance of new data points
    if sample_weight is not None:
        n_new = float(sample_weight.sum())
        new_mu = np.average(X, axis=0, weights=sample_weight / n_new)
        new_var = np.average((X - new_mu) ** 2, axis=0,
                             weights=sample_weight / n_new)
    else:
        n_new = np.sum(~np.isnan(X), axis=0)
        new_var = np.var(X, axis=0)
        new_mu = np.mean(X, axis=0)

    if np.sum(n_past) == 0:
        return new_mu, new_var

    n_total = n_past + n_new

    # Combine mean of old and new data, taking into consideration
    # (weighted) number of observations
    total_mu = (n_new * new_mu + n_past * mu) / n_total

    # Combine variance of old and new data, taking into consideration
    # (weighted) number of observations. This is achieved by combining
    # the sum-of-squared-differences (ssd)
    old_ssd = n_past * var
    new_ssd = n_new * new_var
    total_ssd = (old_ssd + new_ssd +
                 (n_past / (n_new * n_total)) * (n_new * mu - n_new * new_mu) ** 2)
    total_var = total_ssd / n_total

    return total_mu, total_var
