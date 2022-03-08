from sqlalchemy.orm import Session

from . import models, schemas


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"

    db_user = models.User(
        email=user.email,
        password=fake_hashed_password,
        first_name=user.first_name,
        last_name=user.last_name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user: schemas.UserBase):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
