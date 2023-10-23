import os
from sqlalchemy import create_engine


class DB:
    # engine = create_engine(f"sqlite:///{os.path.join(os.getcwd(), 'database/test_data.database')}", echo=True)
    engine = create_engine("sqlite://", echo=True)

