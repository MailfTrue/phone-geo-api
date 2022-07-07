from fastapi import FastAPI, Depends

from db.base import get_session, database
from sqlalchemy.ext.asyncio import AsyncSession
import schemas
import crud

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/{phone}', response_model=schemas.Person)
async def get_user(phone: str, db: AsyncSession = Depends(get_session)):
    return await crud.get_person_by_phone(db, phone)


if __name__ == '__main__':
    app.run()
