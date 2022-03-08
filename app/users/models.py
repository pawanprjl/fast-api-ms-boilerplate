from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=False)
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
