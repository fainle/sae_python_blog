# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import DateTime, Column, func

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
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'MyISAM'}


Base = declarative_base(cls=_Base)


def timestamp_mixin(cls):
    """
    Model column: timestamp mixin decorator.
    """

    cls.created_at = Column(DateTime, default=func.now(), nullable=False)
    cls.updated_at = Column(DateTime, default=func.now(), nullable=False)

    return cls