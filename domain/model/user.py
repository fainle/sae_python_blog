# -*- coding: utf-8 -*-
from domain.model import Base, timestamp_mixin
from sqlalchemy import Column, Integer, String


@timestamp_mixin
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    nickname = Column(String(20))
    password = Column(String(40))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<User('%s','%s')>" % (self.id, self.email)