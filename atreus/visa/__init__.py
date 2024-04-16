import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse
from tenacity import retry, stop_after_attempt, wait_fixed
import logging


from atreus.common import _read_secret
from atreus.settings import settings

vop_auth = {
    "username": _read_secret("vop-authUsername"),
    "password": _read_secret("vop-authPassword"),
}

auth = (vop_auth["username"], vop_auth["password"])
cert = (
    f"{settings.secrets_path}/vop-clientCert",
    f"{settings.secrets_path}/vop-clientKey",
)
base_url = "https://api.visa.com/vop/v1"

router = APIRouter()


@router.get("/vop/helloworld", response_class=PlainTextResponse)
@retry(stop=stop_after_attempt(10), wait=wait_fixed(30))
def VisaHelloWorld(auth: str) -> PlainTextResponse:
    if auth:
        r = requests.get(
            "https://api.visa.com/vdp/helloworld",
            auth=auth,
            cert=cert,
            headers={"Content-Type": "application/json"},
        )
        r.raise_for_status()
        return PlainTextResponse(r.text)
    else:
        return PlainTextResponse("Access Denied")


@router.get("/vop/gettransaction", response_class=JSONResponse)
@retry(stop=stop_after_attempt(10), wait=wait_fixed(30))
def VisaGetTransaction(
    auth: str, transaction_amount: float, transaction_date: str, user_key: str, community_code: str
) -> JSONResponse:
    if auth:
        r = requests.post(
            f"{base_url}/users/gettransaction",
            auth=auth,
            cert=cert,
            headers={"Content-Type": "application/json"},
            json={
                "transactionAmount": transaction_amount,
                "transactionDate": transaction_date,
                "userKey": user_key,
                "communityCode": community_code,
            },
        )
        r.raise_for_status()
        return JSONResponse(r.json())
    else:
        return PlainTextResponse("Access Denied")


@router.get("/vop/merchantsearch", response_class=JSONResponse)
@retry(stop=stop_after_attempt(10), wait=wait_fixed(30))
def VisaGetMerchant(
    auth: str, community_code: str, merchant_name: str, country_code: int, postal_code: str
) -> JSONResponse:
    if auth:
        r = requests.get(
            f"{base_url}/merchants/search/details",
            auth=auth,
            cert=cert,
            headers={"Content-Type": "application/json"},
            params={
                "communityCode": community_code,
                "merchantName": merchant_name,
                "merchantCountryCode": country_code,
                "merchantPostalCode": postal_code,
            },
        )
        r.raise_for_status()
        return JSONResponse(r.json())
    else:
        return PlainTextResponse("Access Denied")


@router.get("/vop/merchantgroup", response_class=JSONResponse)
@retry(stop=stop_after_attempt(10), wait=wait_fixed(30))
def VisaSearchMerchantGroup(auth: str, community_code: str) -> JSONResponse:
    if auth:
        r = requests.get(
            f"{base_url}/merchants/groups?communityCode={community_code}",
            auth=auth,
            cert=cert,
            headers={"Content-Type": "application/json"},
        )
        r.raise_for_status()
        return JSONResponse(r.json())
    else:
        return PlainTextResponse("Access Denied")


@router.get("/vop/offercommunity", response_class=JSONResponse)
@retry(stop=stop_after_attempt(10), wait=wait_fixed(30))
def VisaOfferCommunity(auth: str, community_code: str) -> JSONResponse:
    if auth:
        r = requests.get(
            f"{base_url}/offers/community?communityCode={community_code}",
            auth=auth,
            cert=cert,
            headers={"Content-Type": "application/json"},
        )
        r.raise_for_status()
        return JSONResponse(r.json())
    else:
        return PlainTextResponse("Access Denied")
