from fastapi import APIRouter, FastAPI
from fastapi.responses import PlainTextResponse

from atreus import amex, givex, stonegate, visa

router = APIRouter()


@router.get("/healthz")
def Healthz() -> PlainTextResponse:
    return PlainTextResponse("healthy")


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router)
    app.include_router(visa.router)
    app.include_router(amex.router)
    app.include_router(stonegate.router)
    app.include_router(givex.router)

    return app
