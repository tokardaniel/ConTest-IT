from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer

from database.models.Base import Base
from database.models.Site import Site

class Partner(Base):
    __tablename__ = "partner"

    id: Mapped[int] = mapped_column(primary_key=True)
    data_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)
    street_name: Mapped[str] = mapped_column(String(60), nullable=False)
    house_number: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    saved: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    deleted: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    error: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
    created_at: Mapped[str] = mapped_column(String(), nullable=False)
    sites: Mapped[List["Site"]] = relationship()
