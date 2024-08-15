from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from schemas import URLCreate, URLResponse
from services import shorten_url, get_original_url
from database import  database

app = FastAPI()

@app.on_event("startup")
async def startup():
    """
    Connect to the database on startup.
    """
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """
    Disconnect from the database on shutdown.
    """
    await database.disconnect()


@app.post("/shorten", response_model=URLResponse)
async def create_short_url(url: URLCreate):
    """
    Shorten a given URL and return a shortened URL and the original URL.
    """
    short_code = await shorten_url(url.original_url)
    return {"short_code": short_code, "original_url": url.original_url}


@app.get("/{short_code}")
async def redirect_to_url(short_code: str):
    """
    Redirect to the original URL associated with a given shortened URL.
    """
    url = await get_original_url(short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.original_url)