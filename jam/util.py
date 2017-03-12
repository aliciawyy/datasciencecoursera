from os import path, mkdir


class SolverBase(object):
    all_data_dir = path.join(path.dirname(__file__), "..", "data")

    def __init__(self, name):
        self.name = name
        class_name = self.__class__.__name__
        ind = class_name.find("Solver")
        self.data_dir = path.join(self.all_data_dir, class_name[:ind].lower())
        if not path.exists(self.data_dir):
            mkdir(self.data_dir)
            if self.name == "sample":
                open(self.get_filename("in"), "w").close()
                open(self.get_filename("out"), "w").close()
        self.n_sample_ = 0

    def _get_file_handler(self, ext):
        op = 'w' if ext == 'out' else 'r'
        return open(self.get_filename(ext), op)

    def get_filename(self, ext):
        return path.join(self.data_dir, self.name + "." + ext)

    def _get_input_file(self):
        f = self._get_file_handler('in')
        self.n_sample_ = int(f.readline())
        return f

    def _iter_input(self):
        with self._get_input_file() as f:
            return iter(f.readlines())

    @staticmethod
    def _split_line_to_list(line, fmt=int):
        return [fmt(s) for s in line.split(" ")]

    def _write_result(self, result, sep=" "):
        assert len(result) == self.n_sample_, \
            "length of result '{}' should be equal to the number of samples " \
            "{} for {}.".format(len(result), self.n_sample_, self.__class__)
        f = self._get_file_handler('out')
        for i, line in enumerate(result, 1):
            f.write("Case #{}:{}{}\n".format(i, sep, line))
        f.close()


def sum_of_int(n, mod=None):
    x = int(n * (n + 1) / 2)
    if mod is not None:
        x = x % mod
    return x


def sum_of_int_square(n, mod=None):
    result = int(n * (n + 1) * (n * 2 + 1) / 6)
    if mod is not None:
        result = result % mod
    return result


def sum_of_int_cube(n, mod=None):
    def _mod(y):
        return y if mod is None else y % mod
    x = int(n * (n + 1) / 2)
    x = _mod(x)
    return _mod(x * x)
