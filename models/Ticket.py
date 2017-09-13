from sqlalchemy import Column, Integer, String
from metadata import Base


class Ticket(Base):
    __tablename__ = "Tickets"
    id = Column(Integer, primary_key=True)
    name = Column(String)
