# README for test solutions
> Written by Jack Hayden upon completion of the test

These files contain each completed task as required: `test_t1.py`(1), `test_t2.py`(2) and `test_t3.py`(3).
The corresponding test file for each of these are denoted as `test_log.py`(1), `test_courts.py`(2) and `test_time.py`(3) respectively.

## How to run the code

All requirements are listed in the `requirements.txt` file in the repository.
All solutions were written with Python 3.11.

## How the code works

### `test_1.py`

The `is_log_line()` function validates line inputs based on three criteria:
1. Type: only `str` is allowed.
2. Length: the line must meet a minimum length of 40 characters.
3. Date validity: it must have a valid date that is assessed with `datetime.strptime`.
If each criterion is met, the function returns `True`.

The `get_dict` function converts the valid lines to a dictionary.
- It first dissects the line in timestamp, log_level and message.
- Then it checks the log_level is in the set of allowed values.
- If so, a dictionary is created from the 3 attributes and returned.

When the file is run with `python3 test_1.py` the console prints the tests were successful.
Additional tests can be run with `pytest test_log.py`.

### `test_2.py`

- `generate_people_list()`: this function returns a list of dictionaries, where each dictionary represents a person with provided attributes from a csv file.
- `make_api_request()`: this function uses the `requests` library to make a get request to the relevant URL.
- `get_nearest_court`: this function extracts a postcode value from a 'person' dictionary and uses the `make_api_request()` function to find all nearby courts. To get a single court of the desired type, it uses the `get_first_valid_court()` function. It then filters this result to create a shorter dictionary representation of the court.
- `get_first_valid_court()`: this function takes a list of dictionaries and returns the first one that meets the 'type' criterion input.
- `generate_report`: this takes a list of people dictionaries, and creates a new dictionary which includes information about the person as well as the nearest court they desire. It returns a list of dictionaries as the output.

In the main block, the report is generated from the `people.csv` file and loaded into a json file as they are very useful files for data transfer.
Tests for this file are in the `test_courts.py` file, which can be run with `pytest`.

### `test_3.py`

This script contains the fixed function `sum_current_time()`.
It contains several guard clauses which verify the input:
- Type: raises an error if it is not a string.
- Length: testing both the length of the raw string and the split string in accordance to standard values.
- Time: ensuring the values fall in the correct 24 hour clock specifications.
It converts the values to integers so they can be used in the `sum()` function.

Unit tests for this file are found in `test_time.py`.

---------------
# Data engineering Python tests

> For interviews in April 2022.

This test is to assess your ability to write Python code and to discuss how you think about coding problems during the interview. Don't worry if you don't complete the whole test - you can still pass the interview.

You should have been introduced to a person you can contact to clarify questions or solve technical issues. If anything is unclear or something is wrong, ask them as soon as possible. Asking questions will not affect how we score you on the test, so it is better to ask sooner rather than later.

You are free to use the internet to solve these tests and you can install additional packages. However, the solutions to this test can be achieved using Python and its standard libraries. Use whatever you're most comfortable with. This coding test was written and tested with python 3.8.

## Working with the code

If you can, clone this repo and work on your solutions on your own computer. 

If you don't have a computer where you can do this, you can [complete the test on Google Colab](https://colab.research.google.com/drive/1jIYgeEKarkr6FHAnys6wVSoTIl24PjW6?usp=sharing) instead. Please create a copy of the notebook before you start.

During the interview we'll ask you to share your screen to show and discuss your solutions. You don't need to push your changes to Github or save them anywhere else.


## Doing the tests

There are 3 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test_3.py

These scripts do not need to be completed in order, but we do recommend you do.

In each script is a comment block starting with `[TODO]`. This lays out what needs to be done to solve the test for that particular script. The remaining comments are there to explain the code and direct you.

### Test 1
This asks you to extract and structure data from the file `sample.log`. You'll need to complete 2 short functions.

When you think you have the answer, run `python test_1.py` and it will be automatically tested.

### Test 2
This asks you do get data from an API and match it with data from the file `people.csv`. 

You're free to approach this however you like. We'll ask you to describe your approach and reasoning during the interview.

### Test 3
This asks you to fix a broken function and then write a unit test for it.
