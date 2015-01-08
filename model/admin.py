# -*- coding: utf-8 -*-
from model import Base
from sqlalchemy import Column, Integer, String


PREFIX = 'v2_'


class Admin(Base):
    __tablename__ = PREFIX + 'admin'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    password = Column(String(40))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<User('%s','%s')>" % (self.id, self.email)