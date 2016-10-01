"""
Common classes and data
"""
import numpy as np


def print_dict_as_repr(one_dict, class_name):
    items = ("{}={!r}".format(k, v) for k, v in one_dict.items())
    return "{}({})".format(class_name, ", ".join(items))


class StringMixin(object):
    def __repr__(self):
        my_dict = dict(self.__dict__)
        for k, v in self.__dict__.items():
            if isinstance(v, (list, np.ndarray)) and len(v) > 10:
                my_dict.pop(k)
        return print_dict_as_repr(my_dict, type(self).__name__)

