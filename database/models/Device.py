from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey, String
from sqlalchemy import Boolean
from sqlalchemy import Integer

from database.models.Base import Base

class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    platform: Mapped[str] = mapped_column(String(50), nullable=False)
    serial_number: Mapped[str] = mapped_column(String(50), nullable=False)
    service: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    saved: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    site_id: Mapped[int] = mapped_column(Integer, ForeignKey("site.id"))
