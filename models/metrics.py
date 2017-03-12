import numpy as np
from sklearn.metrics import matthews_corrcoef


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(- x))


def mcc(tp, tn, fp, fn):
    sup = tp * tn - fp * fn
    inf = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    if inf == 0:
        return 0
    else:
        return sup / np.sqrt(inf)


def eval_mcc(y_true, y_prob, show=False):
    idx = np.argsort(y_prob)
    y_true = np.array(y_true, dtype=int)
    y_true_sort = y_true[idx]
    n = y_true.shape[0]
    nump = 1.0 * np.sum(y_true)  # number of positive
    numn = n - nump  # number of negative
    tp = nump
    tn = 0.0
    fp = numn
    fn = 0.0
    best_mcc = 0.0
    best_id = -1
    mccs = np.zeros(n)
    for i in range(n):
        if y_true_sort[i] == 1:
            tp -= 1.0
            fn += 1.0
        else:
            fp -= 1.0
            tn += 1.0
        new_mcc = mcc(tp, tn, fp, fn)
        mccs[i] = new_mcc
        if new_mcc >= best_mcc:
            best_mcc = new_mcc
            best_id = i
    best_proba = y_prob[idx[best_id]]
    y_pred = (y_prob > best_proba).astype(int)
    final_mcc = matthews_corrcoef(y_true, y_pred)
    if show:
        return best_proba, final_mcc, y_pred
    else:
        return final_mcc


def eval_mcc0(y_true, y_prob, show=False):
    return matthews_corrcoef(y_true, (y_prob > 0.005) * 1)
