import os
from sqlalchemy import create_engine

from models.Partner import Partner
from models.Device import Device
from models.Site import Site
from models.Base import Base

# setup
engine = create_engine(f"sqlite:///{os.path.join(os.getcwd(), 'database/test_data.database')}", echo=True)

# migrate
Base.metadata.create_all(engine)
