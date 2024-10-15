from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from app.common.middleware.logging_middleware import LoggingMiddleware
from app.common.middleware.process_time_middleware import ProcesstimeMiddleware
from app.endpoint.sandbox01 import sandbox01
from app.endpoint.sandbox02 import sandbox02
from app.endpoint.sandbox03 import sandbox03
from app.endpoint.sandbox04 import sandbox04

app = FastAPI()

# ミドルウェア
app.add_middleware(LoggingMiddleware)
app.add_middleware(ProcesstimeMiddleware)
app.add_middleware(SessionMiddleware, secret_key="my-session", https_only=True)

# 各ルートを追加
app.include_router(sandbox01.router)
app.include_router(sandbox02.router)
app.include_router(sandbox03.router)
app.include_router(sandbox04.router)

# 静的ファイル
app.mount("/", StaticFiles(directory="static"), name="static")
