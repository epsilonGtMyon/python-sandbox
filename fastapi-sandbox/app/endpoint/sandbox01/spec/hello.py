from typing import Optional
from pydantic import BaseModel


class HelloRequest(BaseModel):
    value01: Optional[str]
    value02: Optional[str]
