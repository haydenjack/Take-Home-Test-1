"""This file contains tests for the test_2.py functions."""

from unittest.mock import patch

from test_2 import generate_people_list, get_first_valid_court, get_nearest_court, generate_report


def test_generate_people_list():
    """Ensures a valid list is created by this function."""
    result = generate_people_list("people.csv")
    assert isinstance(result, list)
    assert "name" in result[0]
    assert "postcode" in result[0]
    assert "court_type" in result[0]


def test_get_first_valid_court():
    """Ensures the function returns the relevant court."""
    test_courts = [
        {"name" : "Test Court",
         "types" : ["Tribunal"]},
        {"name" : "Britain High Court",
         "types" : ["Tribunal","High Court"]}
         ]
    assert get_first_valid_court(test_courts, "High Court") == {"name" : "Britain High Court",
                                                                "types" : ["Tribunal","High Court"]}


def test_get_first_valid_court_no_match():
    """Ensures the function returns None if no match found."""
    test_courts = [
        {"name" : "Test Court",
         "types" : ["Tribunal"]},
        {"name" : "Britain High Court",
         "types" : ["Tribunal","High Court"]}
         ]
    assert get_first_valid_court(test_courts, "County Court") is None


@patch("test_2.make_api_request")
def test_get_nearest_court_no_types(mock_make_api_request):
    """Ensures get_nearest_court returns error message if none found."""
    mock_make_api_request.return_value = [
        {"name" : "Test Court",
         "types" : ["Tribunal"]},
        {"name" : "Britain High Court",
         "types" : ["Tribunal","High Court"]}
         ]
    test_person = {"postcode" : "EH39PD",
                   "court_type" : "Weird Court"}
    assert get_nearest_court(test_person) == {"error" : "No relevant court found."}


@patch("test_2.get_nearest_court")
def test_generate_report(mock_get_nearest_court):
    """Tests that the report function generates the correct information."""
    mock_get_nearest_court.return_value = {"name" : "Britain High Court",
                                           "dx_number": "97345 Southwark 3",
                                           "distance": 1.37}
    people = [{"name": "Jack Hayden", "postcode" : "EH3606", "court_type" : "High Court"}]

    assert generate_report(people) == [{"name": "Jack Hayden",
                                        "court_type": "High Court",
                                        "home_postcode": "EH3606",
                                        "nearest_relevant_court": "Britain High Court",
                                        "dx_number": "97345 Southwark 3",
                                        "distance": 1.37}]
