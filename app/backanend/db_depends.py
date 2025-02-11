from app.backanend.db import Session


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

