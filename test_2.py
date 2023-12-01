# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


import requests
import json


BASE_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="


def generate_people_list(filepath: str) -> list[dict]:
    """Turns a csv file into a list of dictionaries."""

    with open(filepath, "r", encoding="utf-8") as f:
        str_list = f.readlines()
    
    people = []
    for string in str_list[1:]:
        string = string.strip("\n")
        name, postcode, court_type = string.split(",")
        person = {"name" : name,
                  "postcode" : postcode,
                  "court_type" : court_type}
        people.append(person)

    return people


def get_first_valid_court(courts: list[dict], court_type: str) -> dict|None:
    """This function returns the closest court that matches the type desired."""

    for court in courts:
        if court_type in court["types"]:
            return court
    return None


def get_nearest_court(person: dict) -> dict:
    """Returns a dictionary with the relevant court information."""

    postcode = person["postcode"]
    court_type = person["court_type"]
    nearest_courts = requests.get(f"{BASE_URL}{postcode}")
    nearest_court = get_first_valid_court(nearest_courts.json(), court_type)
    if nearest_court:
        filtered_court = {}
        filtered_court["name"] = nearest_court.get("name")
        filtered_court["dx_number"] = nearest_court.get("dx_number")
        filtered_court["distance"] = nearest_court.get("distance")
        return filtered_court
    return {"error" : "No relevant court found."}


def generate_report(people: list[dict]) -> dict:
    """Creates a dictionary of relevant court information for each person."""
    
    report = []
    for person in people:
        person_report = {
            "name" : person["name"],
            "court_type" : person["court_type"],
            "home_postcode" : person["postcode"]
        }
        court = get_nearest_court(person)
        if court.get("error"):
            person_report["error"] = court["error"]
        else:
            person_report["nearest_relevant_court"] = court["name"]
            person_report["dx_number"] = court["dx_number"]
            person_report["distance"] = court["distance"]
        report.append(person_report)

    return report


if __name__ == "__main__":
    # [TODO]: write your answer here

    people = generate_people_list("people.csv")

    report = generate_report(people)

    with open("report.json", "w") as f:
        json.dump(report, f)
