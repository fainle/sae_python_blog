# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms import TextField, TextAreaField, validators, HiddenField, IntegerField, SelectField
from wtforms.validators import Required, Length, ValidationError, Email
from domain.model.topic import Category


class CategoryForm(Form):
    """
    category form
    """
    id = HiddenField('id', default=0)
    name = TextField('name', validators=[
        Required(u'分类名称不能为空'),
        Length(min=2, max=20, message=u'分类名称不能太长')
    ])


class TopicForm(Form):
    """
    topic form
    """
    title = TextField('title', validators=[
        Required(u'标题不能为空')
    ])
    content = TextAreaField('content', validators=[
        Required(u'内容不能为空')
    ])
    priority = IntegerField('priority', default=0)
    category_id = SelectField('category_id', choices=[], coerce=int)
    tag = TextField('tag', default='')