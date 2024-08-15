from sqlalchemy import Table, Column, String, Integer
from database import metadata, engine

# defining the 'urls' table
urls = Table(
    "urls",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("original_url", String, nullable=False),
    Column("short_code", String, unique=True, index=True, nullable=False),
)


# creating all tables defined in the metadata, using provided SQLAlchemy engine imported from database
metadata.create_all(engine)
