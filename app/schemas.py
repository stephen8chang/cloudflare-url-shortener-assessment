from pydantic import BaseModel

class ShortenRequest(BaseModel):
    long_url: str

class ShortenResponse(BaseModel):
    short_url: str
