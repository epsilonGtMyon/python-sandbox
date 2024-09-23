from typing import Optional
from pydantic import BaseModel


class RegisterRequest(BaseModel):
    value01: Optional[str]
    value02: Optional[str]
