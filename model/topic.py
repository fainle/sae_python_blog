# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref
from model import Base, timestamp_mixin


PREFIX = 'v2_'  # table prefix


class Category(Base):
    """
    Category model
    """
    __tablename__ = PREFIX + 'topic_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), default='')
    num = Column(Integer, default=0)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<topoc_category('%s')>" % (self.name, self.name)


@timestamp_mixin
class Topic(Base):
    """
    topic model
    """
    __tablename__ = PREFIX + 'topic'

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    content = Column(Text)
    category_id = Column(Integer, default=0)
    priority = Column(Integer, default=0)
    tag = Column(String(200), default='')
    count = relationship('TopicCount', lazy=True, uselist=False, backref='topic')  # one to one

    def __init__(self, title):
        self.title = title
        self.count = TopicCount()

    def __repr__(self):
        return "<topic('%s','%s')>" % (self.id, self.title)


class TopicTag(Base):
    """
    topic tag model
    """

    __tablename__ = PREFIX + 'topic_tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), default='')
    num = Column(Integer, default=0)

    def __init__(self, name):
        self.name = name
        self.num = 1

    def __repr__(self):
        return "<topic('%s','%s')>" % (self.id, self.name)


class TopicCount(Base):
    """
    topic count
    """

    __tablename__ = PREFIX + 'topic_count'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey(PREFIX + 'topic.id'))
    views = Column(Integer, default=0)
    reply_num = Column(Integer, default=0)


class TopicToTag(Base):
    """
    topic and tag relationships
    """
    __tablename__ = PREFIX + 'topic_tag_relationships'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)

    def __init__(self, topic_id, tag_id):
        self.topic_id = topic_id
        self.tag_id = tag_id


@timestamp_mixin
class TopicReply(Base):
    """
    topic reply
    """
    __tablename__ = PREFIX + 'topic_reply'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, default=0)
    user_id = Column(Integer, default=0)
    content = Column(Text)

    def __init__(self, content):
        self.content = content