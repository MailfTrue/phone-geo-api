from sqlalchemy import Column, DECIMAL, Date, DateTime, Index, Integer
from sqlalchemy.dialects.mysql import CHAR, INTEGER, VARCHAR

from db.base import Base


class Person(Base):
    __tablename__ = 'people'
    __table_args__ = (
        Index('INDX_PARTITION', 'id', 'region_id', unique=True),
    )

    id = Column(Integer, primary_key=True, nullable=False)
    address_city = Column(VARCHAR(255), nullable=False, index=True)
    address_street = Column(VARCHAR(255), index=True)
    address_house = Column(VARCHAR(60), index=True)
    address_entrance = Column(VARCHAR(60), index=True)
    address_floor = Column(VARCHAR(60), index=True)
    address_office = Column(VARCHAR(60), index=True)
    address_comment = Column(VARCHAR(1000), index=True)
    address_full = Column(VARCHAR(1000), index=True)
    address_short = Column(VARCHAR(1000), index=True)
    location_latitude = Column(DECIMAL(10, 6), nullable=False)
    location_longitude = Column(DECIMAL(10, 6), nullable=False)
    currency = Column(CHAR(3), nullable=False)
    amount_client_paid = Column(Integer)
    user_id = Column(Integer, nullable=False)
    yandex_uid = Column(VARCHAR(255))
    user_address_id = Column(Integer)
    crm_comment = Column(VARCHAR(1000))
    first_name = Column(VARCHAR(255), nullable=False, index=True)
    phone_number = Column(VARCHAR(255), nullable=False, index=True)
    user_agent = Column(VARCHAR(512), index=True)
    created_at = Column(DateTime, nullable=False)
    address_doorcode = Column(VARCHAR(20))
    region_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    birth_date = Column(Date)
    SEX = Column(CHAR(1))
