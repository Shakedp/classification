import pytest

from tests.base import base


@pytest.mark.parametrize('test_data_dir_name',
                         [
                             'test_1',
                             'test_2',
                             'test_3',
                             'test_4',
                             'test_combined'
                         ])
def test_sanity(test_data_path, test_data_dir_name):
    base(test_data_path, test_data_dir_name)
