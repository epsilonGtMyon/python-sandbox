import os
from typing import Optional
from dotenv import load_dotenv

# いろいろ設定できるけど、これだと.envから読み取る
load_dotenv()

env_value01 = os.getenv("ENV_VALUE01")
env_value02 = os.getenv("ENV_VALUE02")

print(env_value01)
print(env_value02)
