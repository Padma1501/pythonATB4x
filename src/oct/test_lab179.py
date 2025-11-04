# API Request - HTTP Request

"""import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests

from allure import title as allure_title

@allure_title("TC#1 - Create Booking CRUD Positive ")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud



# To make Request
# URL
# Method POST
# Headers - Content-type-Application/json
# payload / Data / Body - Dict / JSON
# Auth(No)
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

     response = requests.post(url + URL, headers=headers, json=payload)
     # Status Code

     assert response.status_code == 200"""

import allure
import pytest
import requests


@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(URL, headers=headers, json=payload)
    print(response.json())
    assert response.status_code == 200

    responseData = response.json()

    # Response Body Verification,
    # Headers

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    # JSON Schema Validation
    # Time response


@allure.title("TC#1 - Create Booking CRUD Negative")
@allure.description("TC#2 - Verify Booking is not created with {} data ")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500


@allure.title("TC#1 - NegativeCreate Booking CRUD Negative")
@allure.description("TC#3 - Verify Booking with totalprice string negative")
@pytest.mark.crud
def test_create_booking_negative_tc3(): # Bug raise to client or dev
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": "padma",
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"

}
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assetions
    