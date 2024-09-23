import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse


router = APIRouter(prefix="/sandbox03")

stream_messages = [
    "こんにちは。",
    "これはストリーミングレスポンスで返すメッセージです。",
    "このメッセージは逐次返却されます。",
    "残り３",
    "残り２",
    "残り１",
    "おわり。",
]


async def gen_message():
    for mes in stream_messages:
        yield mes
        await asyncio.sleep(0.5)

@router.post("/streaming")
async def streaming():
    return StreamingResponse(
        gen_message(),
        media_type="text/event-stream",
    )
