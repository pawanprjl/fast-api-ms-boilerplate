from . import SessionLocal


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
