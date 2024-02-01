from fastapi import FastAPI

from atreus import healthcheck
from atreus.amex import route as amex
from atreus.givex import givex
from atreus.stonegate import stonegate as sgg
from atreus.visa import vop


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(healthcheck.router)
    app.include_router(vop.router)
    app.include_router(amex.router)
    app.include_router(sgg.router)
    app.include_router(givex.router)

    return app
