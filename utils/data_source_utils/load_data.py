import os
import sys
import random
import tempfile
from dotenv import load_dotenv
from exceptiongroup import catch
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

sys.path.insert(0, os.getcwd())

from utils.data_source_utils.download_data import DownloadData
from database.classes.DB import DB
from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device

load_dotenv(os.path.join(os.getcwd(), ".env"))
# engine = create_engine(f"sqlite:///{os.path.join(os.getcwd(), 'database/test_data.database')}", echo=True)
# engine = create_engine("sqlite://")

class LoadData(DB):

    def __init__(self) -> None:
        self.users: list[dict] = []
        self.devices: list[dict] = []

    def load(self, size=10):
        self.users = DownloadData.download(url = os.getenv("RANDOM_USERS_API").format(size=size))
        self.devices = DownloadData.download(url = os.getenv("RANDOM_DEVICES_API").format(size=size))

        if len(self.users) != len(self.devices):
            raise Exception("userek számának meg kell egyeznie a device-ok számával")

        with Session(self.engine) as session:
            for (user, d_device) in zip(self.users, self.devices):
                partner = Partner(
                    data_id=user.get("id"),
                    first_name=user.get("first_name"),
                    last_name=user.get("last_name"),
                    city=user.get("address")["city"],
                    zip_code=user.get("address")["zip_code"],
                    street_name=user.get("address")["street_name"],
                    house_number="1234",
                    email=user.get("email"),
                )

                site = Site(
                    city=user.get("address")["city"],
                    zip_code=user.get("address")["zip_code"],
                    street_name=user.get("address")["street_name"],
                    house_number="1234"
                )

                device = Device(
                    manufacturer=d_device.get("manufacturer"),
                    model=d_device.get("model"),
                    platform=d_device.get("platform"),
                    serial_number=d_device.get("serial_number"),
                    service=d_device.get("service")
                )

                site.devices.append(device)
                partner.sites.append(site)
                session.add(partner)


            session.commit()

if __name__ == '__main__':
    l = LoadData()
    l.load()
