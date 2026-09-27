# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())