from collections import Counter

import pandas
from src import print_vars


class CustomClass:
    pass


LibraryClass = Counter


def test_example():
    a = 1
    b = CustomClass()
    c = [1, 2, 3]
    d = pandas.read_csv("tests/my_file.csv")
    print_vars()
