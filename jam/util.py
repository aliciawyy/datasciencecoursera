from os import path


class SolverBase:
    all_data_dir = path.join(path.dirname(__file__), "..", "data")

    def __init__(self, name):
        self.name = name
        class_name = self.__class__.__name__
        ind = class_name.find("Solver")
        self.data_dir = path.join(self.all_data_dir, class_name[:ind].lower())
        self.n_sample_ = 0

    def _get_file_handler(self, ext):
        op = 'w' if ext == 'out' else 'r'
        return open(path.join(self.data_dir, self.name + "." + ext), op)

    def _get_input_file(self):
        f = self._get_file_handler('in')
        self.n_sample_ = int(f.readline())
        return f

    def _enumerate_input(self):
        with self._get_input_file() as f:
            return iter(enumerate(f.readlines()))

    def _write_result(self, result, sep=" "):
        f = self._get_file_handler('out')
        for i, line in enumerate(result, 1):
            f.write("Case #{}:{}{}\n".format(i, sep, line))
        f.close()

