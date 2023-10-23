from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import Select
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

    @classmethod
    def get_all_sites(self) -> List[Site]:
        stmt = Select(Site)
        sites: List[Site] = []

        with Session(self.engine) as session:
            for site in session.execute(stmt).fetchall():
                sites.append(site[0])

        return sites

    def get_partner_by_id(self, id: int) -> Partner:
        stmt = Select(Partner).where(Partner.id == id)

        with Session(self.engine) as session:
            return session.execute(stmt).first()[0]

    def get_sites_by_id(self, id: int) -> List[Site]:
        stmt = Select(Site).where(Site.id == id)
        sites = List[Site]

        with Session(self.engine) as session:
            for site in session.execute(stmt).fetchall():
                site.append(site[0])

        return sites
