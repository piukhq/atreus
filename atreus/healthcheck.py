from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/healthz")
def Healthz() -> PlainTextResponse:
    return PlainTextResponse("healthy")
