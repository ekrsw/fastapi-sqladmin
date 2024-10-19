import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

logger = logging.getLogger(__name__)

try:
    async_engine = create_async_engine(
        settings.get_database_url(is_async=True),
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    async_session_factory = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=async_engine,
        class_=AsyncSession,
    )
except Exception as e:
    import traceback

    traceback.print_exc()
    logger.critical(f"DB connection error. detail={e}")


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """async用のdb-sessionの作成."""
    async with async_session_factory() as db:
        try:
            yield db
            await db.commit()
        except Exception:
            await db.rollback()
        finally:
            await db.close()
