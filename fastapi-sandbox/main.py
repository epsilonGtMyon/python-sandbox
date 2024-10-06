from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.common.middleware.logging_middleware import LoggingMiddleware
from app.common.middleware.process_time_middleware import ProcesstimeMiddleware
from app.endpoint.sandbox01 import sandbox01
from app.endpoint.sandbox02 import sandbox02
from app.endpoint.sandbox03 import sandbox03

app = FastAPI()

# ミドルウェア
app.add_middleware(LoggingMiddleware)
app.add_middleware(ProcesstimeMiddleware)

# 各ルートを追加
app.include_router(sandbox01.router)
app.include_router(sandbox02.router)
app.include_router(sandbox03.router)

# 静的ファイル
app.mount("/", StaticFiles(directory="static"), name="static")
