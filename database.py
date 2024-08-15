from sqlalchemy import create_engine, MetaData
from databases import Database
import psycopg2

import getpass  # for hidden passwords in terminal
import sys

# PostgreSQL database configuration
DATABASE_NAME = input("Enter your database name that is Already created OR you want to create <<< default - url_shortner : ") or "url_shortner"
USER = input("Enter your user name for PostgreSQL <<< default - postgres : ") or "postgres"
PASSWORD = getpass.getpass("Enter your password for PostgreSQL : ")
HOST = "localhost"
PORT = input("Enter your port <<< defualt - 5432 : ") or "5432"


def create_database_if_not_exists():
    """
    Creates a PostgreSQL database if it does not already exist.

    This function connects to the PostgreSQL server using the default 'postgres' database.
    It checks whether the specified database exists and creates it if it does not.
    The function handles potential exceptions and prints messages indicating the outcome.

    Steps:
    1. Connects to the PostgreSQL server using the provided credentials.
    2. Checks if the database already exists.
    3. If the database does not exist, it creates a new one.
    4. Handles exceptions related to database creation and connection errors.
    5. Ensures that the connection and cursor are properly closed.

    Exceptions:
    - psycopg2.errors.DuplicateDatabase: Raised if the database already exists, although this exception is handled gracefully.
    - Exception: Catches all other exceptions that may occur during database connection or creation.

    Requirements:
    - Ensure that the following variables are defined with appropriate values:
      USER: PostgreSQL username
      PASSWORD: PostgreSQL password
      HOST: PostgreSQL host address
      PORT: PostgreSQL port number
      DATABASE_NAME: Name of the database to be created

    """
    conn = None
    try:
        conn = psycopg2.connect(dbname='postgres', user=USER, password=PASSWORD, host=HOST, port=PORT)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{DATABASE_NAME}'")
        if cursor.fetchone() is None:
            cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")
            print(f"Database {DATABASE_NAME} created.")
        else:
            print(f"Database {DATABASE_NAME} already exists.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"database {DATABASE_NAME} already exists.")
    except Exception as e:
        print(f"Error creating database: {e}")
        sys.exit("Stop the Application by pressing `Ctrl+c` .")
    finally:
        if conn:
            cursor.close()
            conn.close()




# calling create_database_if_not_exists
create_database_if_not_exists()


# URL for connecting to database
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"

# initializing the database object for asynchronous operations
database = Database(DATABASE_URL)

# creating MetaData instance to hold schema information
metadata = MetaData()

# creating an SQLAlchemy engine for database interactions
engine = create_engine(DATABASE_URL)

