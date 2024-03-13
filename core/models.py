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
if __name__ == '__main__':
    Base.metadata.create_all(engine)