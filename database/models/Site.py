from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, ForeignKeyConstraint, String
from sqlalchemy import Boolean
from sqlalchemy import Integer

from models.Base import Base
from models.Device import Device

class Site(Base):
    __tablename__ = "site"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(60), nullable=False)
    street_name: Mapped[str] = mapped_column(String(60), nullable=False)
    house_number: Mapped[str] = mapped_column(String(10), nullable=False)
    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"))
    devices: Mapped[List["Device"]] = relationship()
