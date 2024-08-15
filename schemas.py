from pydantic import BaseModel

class URLCreate(BaseModel):
    """
    Model for creating a new URL.
    """
    original_url: str


class URLResponse(BaseModel):
    """
    Model for returning a shortened URL along with its original URL.
    """
    short_code: str
    original_url: str
