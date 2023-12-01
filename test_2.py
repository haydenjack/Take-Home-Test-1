"""This script generates a json report containing court locations & distances for
 individuals in people.csv based on their home postcode and desired court type."""


import json
import requests


BASE_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="
REQ_TIMEOUT = 10
NOT_FOUND_SC = 404
INTERNAL_ERROR_SC = 500
BAD_REQUEST_SC = 400
UNAUTHORISED_SC = 401


def generate_people_list(filepath: str) -> list[dict]:
    """Turns a csv file with personal info into a list of dictionaries."""

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
        if court_type in court.get("types"):
            return court
    return None


def make_api_request(url: str) -> json:
    """Sends a get request to the provided URL."""

    response = requests.get(url, timeout=REQ_TIMEOUT)
    if response.status_code == NOT_FOUND_SC:
        raise ConnectionError("Not found")
    if response.status_code == INTERNAL_ERROR_SC:
        raise ConnectionError("Internal server error")
    if response.status_code == BAD_REQUEST_SC:
        raise ConnectionError("Bad request")
    if response.status_code == UNAUTHORISED_SC:
        raise ConnectionError("Unauthorised connection")
    return response.json()


def get_nearest_court(person: dict) -> dict:
    """Returns a dictionary with the relevant court information."""

    postcode = person["postcode"]
    court_type = person["court_type"]
    nearest_courts = make_api_request(f"{BASE_URL}{postcode}")
    nearest_court = get_first_valid_court(nearest_courts, court_type)
    if nearest_court:
        filtered_court = {}
        filtered_court["name"] = nearest_court.get("name")
        filtered_court["dx_number"] = nearest_court.get("dx_number")
        filtered_court["distance"] = nearest_court.get("distance")
        return filtered_court
    return {"error" : "No relevant court found."}


def generate_report(people: list[dict]) -> list[dict]:
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
            person_report["distance"] = court["distance"]
            if court.get("dx_number"):
                person_report["dx_number"] = court["dx_number"]
        report.append(person_report)

    return report


if __name__ == "__main__":

    people = generate_people_list("people.csv")

    report = generate_report(people)

    with open("report.json", "w", encoding="utf-8") as output:
        json.dump(report, output)
