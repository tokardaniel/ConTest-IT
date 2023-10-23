import os
import sys
from sqlalchemy import create_engine
from database.classes.DB import DB

sys.path.insert(0, os.getcwd())

from database.models.Base import Base

from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device

class Migration(DB):

    def __init__(self, connection_str: str = None):
        self.connection_str = connection_str

    # migrate
    def run(self):
        if self.connection_str is not None:
            # save database to filesystem
            self.engine = create_engine(f"sqlite:///{os.path.join(os.getcwd(), 'database/test_data.database')}", echo=True)

        Base.metadata.create_all(self.engine)

if __name__ == "__main__":
    migration = Migration()
    migration.run()
