from sqlalchemy import Boolean, Column, Integer, String
from .database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    username=Column(String)
    social_media=Column(String)
    is_active = Column(Boolean, default=True)
class Threads(Base):
    __tablename__ = "therapists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    phone = Column(String, index=True)
    qualification = Column(String, index=True)
    description = Column(String, index=True)
class messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    user_id = Column(Integer, index=True)
    thread_id = Column(Integer, index=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)