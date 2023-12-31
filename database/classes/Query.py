from typing import List, Union
from sqlalchemy.orm import Session
from sqlalchemy import Select
from sqlalchemy import Update
from sqlalchemy.orm import joinedload
from database.classes.DB import DB
from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device


class Query(DB):

    def get_all_partners(self) -> List[Partner]:
        stmt = Select(Partner)
        partners: List[Partner] = []

        with Session(self.engine) as session:
            for partner in session.execute(stmt).fetchall():
                partners.append(partner[0])

        return partners

    def get_all_partners_full_join(self) -> Union[List[Partner], List[Site], List[Device]]:
        with Session(self.engine) as session:
            return session.query(Partner).options(joinedload(Partner.sites).subqueryload(Site.devices)).all()


    def get_all_sites(self) -> List[Site]:
        stmt = Select(Site)
        sites: List[Site] = []

        with Session(self.engine) as session:
            for site in session.execute(stmt).fetchall():
                sites.append(site[0])

        return sites

    def get_all_devices(self) -> List[Device]:
        stmt = Select(Device)
        devices: List[Device] = []

        with Session(self.engine) as session:
            for device in session.execute(stmt).fetchall():
                devices.append(device)

        return devices

    def get_partner_by_id(self, id: int) -> Partner:
        stmt = Select(Partner).where(Partner.id == id)

        with Session(self.engine) as session:
            return session.execute(stmt).first()[0]

    def get_partner_by_test_id(self, id: int) -> Partner:
        stmt = Select(Partner).where(Partner.test_id == id)

        with Session(self.engine) as session:
            return session.query(Partner).options(joinedload(Partner.sites).subqueryload(Site.devices)).where(Partner.test_id == id).first()

    # egy adottt parnerhez tartozó eszközöket adja vissza email alapján
    def get_device_by_partner_email(self, email: str) -> List[Device]:
        stmt = Select(Partner).where(Partner.email == email)

        with Session(self.engine) as session:
            return session.execute(stmt).first().devices

    def get_sites_by_id(self, id: int) -> List[Site]:
        stmt = Select(Site).where(Site.id == id)
        sites: List[Site] = []

        with Session(self.engine) as session:
            for site in session.execute(stmt).fetchall():
                site.append(site[0])

        return sites

    def get_device_by_id(self, id: int) -> List[Device]:
        stmt = Select(Device).where(Device.id == id)
        devices: List[Device] = []

        with Session(self.engine) as session:
            for device in session.execute(stmt).fetchall():
                devices.append(device)

        return devices

    def get_all_service_devices_of_partner(self) -> List[Partner]:
        with Session(self.engine) as session:
            return session.query(Partner).options(joinedload(Partner.sites).subqueryload(Site.devices)).where(Device.service == True).all()

    def get_all_service_devices_of_partner_by_test_id(self, id: int) -> List[Partner]:
        with Session(self.engine) as session:
            return session.query(Partner).options(joinedload(Partner.sites).subqueryload(Site.devices)).where(
                Device.service == True and Partner.test_id == id
            ).all()

    def update_service_status(self, device: Device) -> None:
        stmt = Update(Device).where(Device.id == device.id).values(service = True)

        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()
