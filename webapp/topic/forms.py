# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms import TextAreaField, IntegerField, SelectField, StringField
from wtforms.validators import Length, DataRequired


class CategoryForm(Form):
	"""
	category form
	"""
	name = StringField('name', validators=[
		DataRequired(u'分类名称不能为空'),
		Length(min=2, max=20, message=u'分类名称不能太长')])
	content = TextAreaField('content')
	num = IntegerField('num')


class TopicForm(Form):
	"""
	topic form
	"""
	title = StringField('title', validators=[DataRequired(u'标题不能为空')])
	content = TextAreaField('content', validators=[DataRequired(u'内容不能为空')])
	priority = IntegerField('priority', default=0)
	category_id = SelectField('category_id', choices=[], coerce=int, default=0)
	tag = StringField('tag', default='')