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
        op = 'r' if ext == 'in' else 'w'
        return file(path.join(self.data_dir, self.name + "." + ext), op)

    def _get_input_file(self):
        f = self._get_file_handler('in')
        self.n_sample_ = int(f.readline())
        return f

    def _write_result(self, result):
        f = self._get_file_handler('out')
        for line in result:
            f.write(line)
        f.close()

