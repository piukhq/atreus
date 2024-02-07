import base64
import hashlib
import hmac
import json
import logging
import time
import uuid
from urllib.parse import urlsplit

import requests
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from atreus.common import connect_to_vault, load_cert_from_vault
from atreus.settings import settings

logger = logging.getLogger(__name__)
router = APIRouter()


def search_amex_merchants(request_body: dict):
    session = requests.Session()
    session.mount(settings.amex_hostname)

    return _call_api("POST", "/marketing/v4/smartoffers/merchant/inquiry_results", session, request_body)


def _call_api(method: str, resource_uri: str, session, data: dict = None):
    client_priv_path, client_cert_path = load_cert_from_vault("amex-cert")

    payload = json.dumps(data)
    headers = _make_headers(method, resource_uri, payload)

    response = getattr(session, method.lower())(
        settings.amex_hostname + resource_uri,
        cert=(client_cert_path, client_priv_path),
        headers=headers,
        data=payload,
        timeout=(3.05, 10),
    )

    return response


def _make_headers(httpmethod: str, resource_uri: str, payload: str) -> dict:
    current_time_ms = str(round(time.time() * 1000))
    nonce = str(uuid.uuid4())
    client_id, client_secret = client_id_and_secret()

    bodyhash = base64.b64encode(
        hmac.new(client_secret.encode(), payload.encode(), digestmod=hashlib.sha256).digest()
    ).decode()

    hash_key_secret = (
        f"{current_time_ms}\n{nonce}\n{httpmethod.upper()}\n"
        f"{resource_uri}\n{urlsplit(settings.amex_hostname).netloc}\n443\n{bodyhash}\n"
    )
    mac = base64.b64encode(
        hmac.new(client_secret.encode(), hash_key_secret.encode(), digestmod=hashlib.sha256).digest()
    ).decode()

    return {
        "Content-Type": "application/json",
        "X-AMEX-API-KEY": client_id,
        "Authorization": f'MAC id="{client_id}",ts="{current_time_ms}"'
        f',nonce="{nonce}",bodyhash="{bodyhash}",mac="{mac}"',
    }


def client_id_and_secret():
    client = connect_to_vault()
    client_id = json.loads(client.get_secret("amex-clientId").value)["value"]
    client_secret = json.loads(client.get_secret("amex-clientSecret").value)["value"]
    return client_id, client_secret


@router.post("/amex/merchant-search")
def amex_merchant_search(auth: str, postal_code: str, merchant_name: str, street: str, city: str, state: str):
    if auth:
        request_body = {
            "partner_id": "AADP0050",
            "postalCode": postal_code,
            "merchantName": merchant_name,
            "street": street,
            "city": city,
            "state": state,
        }
        r = search_amex_merchants(request_body)
        return json.loads(r)
    else:
        return PlainTextResponse("Access Denied")
