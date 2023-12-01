"""This file contains unit tests for the test_1.py file."""

import pytest

from test_1 import is_log_line, get_dict


def test_is_log_line_valid_date():
    """Ensures function can handle valid inputs."""
    assert is_log_line("03/11/21 08:51:01 INFO :.main: *************** RSVP Agent started") == True


def test_is_log_line_invalid_date():
    """Ensures function can handle invalid dates."""
    assert is_log_line("03/11 08:51 INFO :.main: *************** RSVP Agent started") == None


def test_is_log_line_invalid_line():
    """Ensures function can handle short lines."""
    assert is_log_line("inserted") == None


def test_is_log_line_empty_input():
    """Ensures function can handle empty input."""
    assert is_log_line("") == None


def test_is_log_line_invalid_type():
    """Ensures function can handle non-string inputs."""
    with pytest.raises(TypeError):
        is_log_line(99)


def test_get_dict_normal_function():
    """Ensures the function can handle normal inputs."""
    assert get_dict("03/11/21 08:51:01 INFO :.main: Using log level 511") == {"timestamp" : "03/11/21 08:51:01",
                                                                                 "log_level" : "INFO",
                                                                                 "message" : ":.main: Using log level 511"}

def test_get_dict_invalid_log_level():
    """Checks identification of invalid log levels."""
    with pytest.raises(ValueError):
        get_dict("03/11/21 08:51:01 NOPE :.main: Using log level 511")


def test_get_dict_invalid_input_str():
    """Checks identification of invalid log levels."""
    with pytest.raises(ValueError):
        get_dict("Using log level 511")
