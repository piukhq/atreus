import csv
import json

import requests

endpoint = "https://uk-bink-mids.azurewebsites.net/api/BinkMIDsWebhook"


def _create_onboards() -> dict:
    payloads = {}
    with open("onboards.csv") as f:
        csvf = csv.reader(f, delimiter=",")
        for row in csvf:
            store_id = row[0]
            issuer = row[1]
            mid = row[2]
            if store_id not in payloads:
                payloads[store_id] = {
                    "visa_mids": [],
                    "mastercard_mids": [],
                    "amex_mids": [],
                }
            if issuer == "visa":
                payloads[store_id]["visa_mids"].append(mid)
            if issuer == "mastercard":
                payloads[store_id]["mastercard_mids"].append(mid)
            if issuer == "amex":
                payloads[store_id]["amex_mids"].append(mid)
    return payloads


def _post_onboards() -> dict:
    data = _create_onboards()
    for key, value in data.items():
        payload = {
            "store_id": key,
            "visa_mids": value["visa_mids"],
            "mastercard_mids": value["mastercard_mids"],
            "amex_mids": value["amex_mids"],
        }
        data = json.dumps(payload)

        print("---")
        print(data)
        response = requests.post(url=endpoint, data=data)
        print(response.status_code)
        print("---")


def _create_offboards():
    payloads = {}
    with open("offboard.csv") as f:
        csvf = csv.reader(f, delimiter=",")
        for row in csvf:
            store_id = row[0]
            if store_id not in payloads:
                payloads[store_id] = {
                    "visa_mids": [],
                    "mastercard_mids": [],
                    "amex_mids": [],
                }
    return payloads


def _post_offboards() -> dict:
    data = _create_offboards()
    for key, _ in data.items():
        payload = {
            "store_id": key,
            "visa_mids": [],
            "mastercard_mids": [],
            "amex_mids": [],
        }
        data = json.dumps(payload)

        print("---")
        print(data)
        response = requests.post(url=endpoint, data=data)
        print(response.status_code)
        print("---")


# _post_onboards(_create_onboards())
_post_offboards(_create_offboards())
