"""This script contains a function that calculates the sum of values in a time string."""

MIN_TIME = 0
MAX_MMSS = 59
MAX_HOUR = 23
VAL_INPUT_LEN = 8
VAL_LIST_LEN = 3


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    if not isinstance(time_str, str):
        raise TypeError("Input must be a string.")

    list_of_nums = time_str.split(":")

    if len(time_str) != VAL_INPUT_LEN or len(list_of_nums) != VAL_LIST_LEN:
        raise ValueError("Format must be HH:MM:SS.")

    list_of_nums = [int(n) for n in list_of_nums]

    if list_of_nums[0] > MAX_HOUR or list_of_nums[1] > MAX_MMSS or list_of_nums[2] > MAX_MMSS:
        raise ValueError("Invalid time supplied.")
    if any(num < MIN_TIME for num in list_of_nums):
        raise ValueError("Invalid time supplied.")

    return sum(list_of_nums)
