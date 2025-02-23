import fire

from app.database import async_engine
from app.models.base import Base
from app.models import User, Todo, Tag, TodoTag


async def create_all_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("created")


if __name__ == "__main__":
    fire.Fire()
