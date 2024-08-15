import string
import random
from models import urls
from database import database


def generate_short_code(length=6):
    """
    function to generate a unique short code of specified length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


async def shorten_url(original_url: str):
    """
    function to shorten a given URL by generating a unique short_code and saving it in the database.
    """
    short_code = generate_short_code()
    query = urls.insert().values(original_url=original_url, short_code=short_code)
    await database.execute(query)
    return short_code


async def get_original_url(short_code: str):
    """
    function for retrieving the entry associated with a given short_code from the database.
    """
    query = urls.select().where(urls.c.short_code == short_code)
    return await database.fetch_one(query)
