from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import *


async def get_users(session: AsyncSession) -> list[City]:
    result = await session.execute(select(City).order_by(City.population.desc()).limit(20))
    return result.scalars().all()

    