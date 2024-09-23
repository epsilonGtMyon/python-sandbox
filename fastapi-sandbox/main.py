from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.endpoint.sandbox01 import sandbox01
from app.endpoint.sandbox02 import sandbox02

app = FastAPI()

# 各ルートを追加
app.include_router(sandbox01.router)
app.include_router(sandbox02.router)

# 静的ファイル
app.mount("/", StaticFiles(directory="static"), name="static")
