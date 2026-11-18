from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import Base


class TaskModel(Base):

    __tablename__ = "users_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)
    is_completed = Column(Boolean, default=False)