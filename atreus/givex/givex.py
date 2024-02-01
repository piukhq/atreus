import json
import logging
import uuid

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from jsonrpclib import jsonrpc

from atreus.common import _read_secret
from atreus.givex.response_models import Givex995Response, Givex996Response
from atreus.settings import settings

logger = logging.getLogger(__name__)
router = APIRouter()

auth = settings.auth
givex_number = settings.givex_number
base_url = "dev-dataconnect.givex.com"
givex_username = _read_secret("givex-username")
givex_password = _read_secret("givex-password")


@router.get("/givex/accounthistory")
def account_history(auth: str, givex_number: str):
    if auth:
        logger.error("On get")

        myuuid = uuid.uuid4()
        givex = jsonrpc.ServerProxy(f"https://{base_url}:50104")
        responses = givex.dc_995("en", str(myuuid), givex_username, givex_password, givex_number, "", "", "Points")

        json_responses = []
        json_responses.append(json.dumps(dict(zip(list(Givex995Response.model_fields.keys()), responses))))
        return json_responses
    else:
        return PlainTextResponse("Access Denied")


@router.get("/givex/accountlookup")
def account_lookup(auth: str, givex_number: str):
    if auth:
        logger.error("On get")

        myuuid = uuid.uuid4()
        givex = jsonrpc.ServerProxy(f"https://{base_url}:50104")
        responses = givex.dc_996("en", str(myuuid), givex_username, givex_password, givex_number)

        json_responses = []
        json_responses.append(json.dumps(dict(zip(list(Givex996Response.model_fields.keys()), responses))))
        return json_responses
    else:
        return PlainTextResponse("Access Denied")
