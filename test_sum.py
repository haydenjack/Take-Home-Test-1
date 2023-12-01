"This file contains unit tests for the sum_current_time function."

import pytest

from test_3 import sum_current_time


def test_sum_current_time_basic():
    "Basic test for the sum function."
    assert sum_current_time("01:02:03") == 6


def test_sum_current_time_bigger():
    "Tests the calculation works for larger sums."
    assert sum_current_time("13:10:50") == 73


def test_sum_current_time_invalid_str():
    "Tests invalid int input raises an ValueError."
    with pytest.raises(ValueError):
        sum_current_time("99")


def test_sum_current_time_int_input():
    "Tests invalid int input raises an ValueError."
    with pytest.raises(TypeError):
        sum_current_time(4)


def test_sum_current_time_dict_input():
    "Tests invalid dict input raises an ValueError."
    with pytest.raises(TypeError):
        sum_current_time({"time": "01:04:03"})


def test_sum_current_time_list_input():
    "Tests invalid dict input raises an ValueError."
    with pytest.raises(TypeError):
        sum_current_time(["1","03","04"])


def test_sum_current_time_empty_input():
    "Tests invalid dict input raises an ValueError."
    with pytest.raises(TypeError):
        sum_current_time()