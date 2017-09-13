from sqlalchemy import Column, Integer, String
from metadata import Base


class Event(Base):
    __tablename__ = "Events"
    id = Column(Integer, primary_key=True)
    name = Column(String)
