from pydantic import BaseModel, constr, condecimal
from datetime import date, datetime


class Person(BaseModel):
    id: int
    address_city: constr(max_length=255)
    address_street: constr(max_length=255) | None
    address_house: constr(max_length=60) | None
    address_entrance: constr(max_length=60) | None
    address_floor: constr(max_length=60) | None
    address_office: constr(max_length=60) | None
    address_comment: constr(max_length=1000) | None
    address_full: constr(max_length=1000) | None
    address_short: constr(max_length=1000) | None
    location_latitude: condecimal(decimal_places=6)
    location_longitude: condecimal(decimal_places=6)
    currency: constr(max_length=3, min_length=3)
    amount_client_paid: int | None
    user_id: int
    yandex_uid: constr(max_length=255) | None
    user_address_id: int | None
    crm_comment: constr(max_length=1000) | None
    first_name: constr(max_length=255)
    phone_number: constr(max_length=255)
    user_agent: constr(max_length=512) | None
    created_at: datetime
    address_doorcode: constr(max_length=20) | None
    region_id: int
    birth_date: date | None
    SEX: constr(min_length=1, max_length=1) | None

    class Config:
        orm_mode = True
