from sqlalchemy import Column, REAL, BigInteger, TEXT, ForeignKey, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
