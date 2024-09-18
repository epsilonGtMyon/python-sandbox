from fastapi import APIRouter


router = APIRouter(prefix= "/sandbox01")


@router.get("/hello")
async def hello():
  return {
    "value": "hello"
  }