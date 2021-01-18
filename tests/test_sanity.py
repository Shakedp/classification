import sys

from tests.base import base


def test_1(test_data_path):
    base(test_data_path, sys._getframe().f_code.co_name)