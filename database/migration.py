import os
import sys
from sqlalchemy import create_engine

sys.path.insert(0, os.getcwd())

from database.models.Base import Base

from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device

# setup
engine = create_engine(f"sqlite:///{os.path.join(os.getcwd(), 'database/test_data.database')}", echo=True)

# migrate
Base.metadata.create_all(engine)
