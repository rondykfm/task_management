from sqlalchemy import Column, String, DateTime, Boolean,Integer
from src.utils.db import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    username = Column(String(150), nullable=False)
    hash_password = Column(String(100), nullable=False)
    email = Column(String(30))
