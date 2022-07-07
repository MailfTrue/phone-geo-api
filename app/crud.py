from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models


async def get_person_by_phone(session: AsyncSession, phone: str):
    result = await session.execute(select(models.Person).filter(models.Person.phone_number == phone))
    return result.scalar()
