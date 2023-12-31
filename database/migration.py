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

    # migrate
    def run(self):
        Base.metadata.create_all(self.engine)

if __name__ == "__main__":
    migration = Migration()
    migration.run()
