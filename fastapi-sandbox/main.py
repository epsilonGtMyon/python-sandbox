from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.endpoint.sandbox01 import sandbox01

app = FastAPI()

# 各ルートを追加
app.include_router(sandbox01.router)

# 静的ファイル
app.mount("/", StaticFiles(directory="static"), name="static")
