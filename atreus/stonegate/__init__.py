import json
import logging
from urllib.parse import urlencode, urljoin

import requests
from fastapi import APIRouter

from atreus.common import _read_secret
from atreus.settings import settings

logger = logging.getLogger(__name__)
router = APIRouter()


base_url = settings.stonegate_atreemo_url
stonegate_auth = {
    "username": _read_secret("stonegate-outbound-compound-key-join")["data"]["username"],
    "password": _read_secret("stonegate-outbound-compound-key-join")["data"]["password"],
}


def call_auth_endpoint():
    url = urljoin(base_url, "token")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "grant_type": "password",
        "username": stonegate_auth["username"],
        "password": stonegate_auth["password"],
    }
    payload = urlencode(payload)

    response = requests.request("POST", url, headers=headers, data=payload)
    bearer_token = f'Bearer {json.loads(response.text)["access_token"]}'
    return bearer_token


@router.get("/sgg/findbyemail")
def find_by_email(email: str):
    url = urljoin(base_url, "api/Customer/FindCustomerDetails")
    bearer_token = call_auth_endpoint()
    payload = json.dumps(
        {
            "SearchFilters": {"Email": email},
            "ResponseFilters": {"LoyaltyDetails": True, "StaffInfo": True, "SupInfo": True},
            "BrandID": "Bink",
        }
    )
    headers = {"Content-Type": "application/json", "Authorization": bearer_token}

    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        return json.loads(response.text)
    except json.decoder.JSONDecodeError as e:
        return {"response_status": response.status_code, "error": str(response.text)}


def get_email_from_query_params(email: str):
    return email if email else None


@router.get("/sgg/findbymembernumber")
def find_by_member_number(member_number: str):
    url = urljoin(base_url, "api/Customer/FindCustomerDetails")
    bearer_token = call_auth_endpoint()
    payload = json.dumps(
        {
            "SearchFilters": {"MemberNumber": member_number},
            "ResponseFilters": {"LoyaltyDetails": True, "StaffInfo": True, "SupInfo": True},
            "BrandID": "Bink",
        }
    )
    headers = {"Content-Type": "application/json", "Authorization": bearer_token}

    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        return json.loads(response.text)
    except json.decoder.JSONDecodeError as e:
        return {"response_status": response.status_code, "error": str(response.text)}
