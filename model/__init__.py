# -*- coding: utf-8 -*-
import sae.const
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import DateTime, Column, func

db_link = 'mysql+mysqldb://' + sae.const.MYSQL_USER + ':' + sae.const.MYSQL_PASS + '@' + sae.const.MYSQL_HOST + ':' + \
          sae.const.MYSQL_PORT + '/' + sae.const.MYSQL_DB + '?charset=utf8'

engine = create_engine(db_link, pool_recycle=10)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class _Base(object):
	"""
	Custom base model.
	"""

	@classmethod
	def get(cls, id):
		"""
		Get object by it's id.
		"""

		return cls.query.get(id)

	@classmethod
	def gets(cls, ids):
		"""
		Get objects by id list.
		"""

		ids = {}.fromkeys(ids).keys()
		if len(ids) > 0:
			return cls.query.filter(cls.id.in_(ids))
		else:
			return []

	@declared_attr
	def __tablename__(cls):
		"""
		Automatic cover model map tablename to lower
		"""

		return cls.__name__.lower()

	# Default table config.
	__table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'MyISAM'}


def timestamp_mixin(cls):
	"""
	Model column: timestamp mixin decorator.
	"""

	cls.created_at = Column(DateTime, default=func.now(), nullable=False)
	cls.updated_at = Column(DateTime, default=func.now(), nullable=False)

	return cls

Base = declarative_base(cls=_Base)
Base.query = db_session.query_property()