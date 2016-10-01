from os import path
import pandas as pd

DATA_PATH = path.dirname(__file__)


def data_reader(filename):
    if not filename.endswith(".csv"):
        filename += ".csv"
    full_filename = path.join(DATA_PATH, filename)
    return pd.read_csv(full_filename)


def load_candidates_to_hire_data():
    return data_reader("candidates_to_hire")
