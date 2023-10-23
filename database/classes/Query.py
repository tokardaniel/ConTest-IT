
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import Select
from sqlalchemy import Join
from database.classes.DB import DB
from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device


class Query(DB):

    def get_partner_by_group_id(self, group_id: str):
        stmt = Select(Partner).where(Partner.group_id == group_id)
        with Session(self.engine) as session:
            session.execute(stmt).fetchall()

    def get_all_partners(self) -> List[object]:
        stmt = Select(Partner)
        partners: List[Partner] = []

        with Session(self.engine) as session:
            for partner in session.execute(stmt).fetchall():
                partners.append(partner[0])

        return partners
