

from fastapi import APIRouter

from app.endpoint.sandbox02.spec.register import RegisterRequest


router = APIRouter(prefix = "/sandbox02")


@router.post("/register")
async def register(req: RegisterRequest):
  return {
    "body": req
  }
