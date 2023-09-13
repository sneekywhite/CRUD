from sqlalchemy import Column, Integer, String
from database import Base


class Person(Base):
    __tablename__ = 'person'

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    



