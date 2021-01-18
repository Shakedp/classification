#!/usr/bin/env python3
import os

import pytest

TESTS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_NAME = 'test_data'
TEST_DATA_PATH = os.path.join(TESTS_DIR_PATH, TEST_DATA_NAME)


@pytest.fixture(scope='session')
def test_data_path():
    return TEST_DATA_PATH