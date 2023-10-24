import os
from sqlalchemy import create_engine


class DB:
    engine = create_engine(os.getenv("DATABASE_CONNECTION_STR"), echo=True)
