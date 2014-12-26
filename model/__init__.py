# -*- coding: utf-8 -*-
from flask import Flask
import sae.const
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, func

db_link = 'mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST + ':' + \
          sae.const.MYSQL_PORT + '/' + sae.const.MYSQL_DB + '?charset=utf8'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_link
app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
app.config['SQLALCHEMY_POOL_SIZE'] = 5

db_session = SQLAlchemy(app)

Base = db_session.Model


def timestamp_mixin(cls):
	"""
	Model column: timestamp mixin decorator.
	"""

	cls.created_at = Column(DateTime, default=func.now(), nullable=False)
	cls.updated_at = Column(DateTime, default=func.now(), nullable=False)

	return cls