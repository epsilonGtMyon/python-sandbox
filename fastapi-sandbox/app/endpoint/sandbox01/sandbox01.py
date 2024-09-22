from typing import Annotated
from fastapi import APIRouter, Query

from app.endpoint.sandbox01.spec.hello import HelloRequest

router = APIRouter(prefix="/sandbox01")


@router.get("/hello")
async def hello(req: Annotated[HelloRequest, Query()]):
    return {
        "resp": {
            "valuea": req.value01,
            "valueb": req.value02,
        }
    }
