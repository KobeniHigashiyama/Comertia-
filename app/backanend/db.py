
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.backanend.config import settings

# Настройки базы данных

# Создание асинхронного движка
engine = create_async_engine(settings.DATABASE_URL)

# Создание фабрики асинхронных сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс для моделей
class Base(DeclarativeBase):
    pass
