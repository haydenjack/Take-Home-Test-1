# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    if not isinstance(time_str, str):
        raise TypeError("Input must be a string.")
    
    list_of_nums = time_str.split(":")

    if len(time_str) != 8 or len(list_of_nums) != 3:
        raise ValueError("Format must be HH:MM:SS.")
    
    list_of_nums = [int(n) for n in list_of_nums]
    return sum(list_of_nums)

