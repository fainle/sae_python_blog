# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, abort, request, redirect
from model import db_session
from model.topic import Topic, Category, TopicTag, TopicToTag
from webapp.topic.forms import TopicForm, CategoryForm
# from webapp.user import is_admin, login_required


topic_page = Blueprint('topic_page', __name__)


@topic_page.route("/topic/<int:id>")
def topic_show(id=1):
	"""
	main page
	"""
	topic = Topic.query.filter(Topic.id == id).first()
	# reply_form = ReplyForm()
	if topic:
		category = Category.query.filter(Category.id == topic.category_id).first()
		# reply = TopicReply.query.filter(TopicReply.topic_id == topic.id).all()
		topic.count.views += 1
		db_session.commit()

	else:
		abort(404)

	return render_template('/topic/show.html', topic=topic, category=category)
# count=topic.count,
# reply_form=reply_form,
#reply=reply,)


def category_count(topic, topic_form):
	if topic.category_id != topic_form.category_id.data and topic.id != 0:
		new_category = Category.query.get(topic_form.category_id.data)
		new_category.num += 1
		old_category = Category.query.get(topic.category_id)
		old_category.num -= 1


@topic_page.route('/topic/add', methods=("POST", "GET"))
@topic_page.route('/topic/add/<int:id>', methods=("POST", "GET"))
# @login_required
# @is_admin
def topic_add(id=0):
	"""
	add topic
	"""
	topic = Topic.query.filter(Topic.id == id).first()
	topic_form = TopicForm(obj=topic)

	category_list = [(0, u"没有分类")]
	category = Category.query.all()
	if category:
		for c in category:
			category_list.append((c.id, c.name))
	topic_form.category_id.choices = category_list

	if request.method == 'POST' and topic_form.validate():
		if topic:
			topic_form.populate_obj(topic)
			category_count(topic, topic_form)  # category count
		else:
			topic = Topic(topic_form.title.data)
			topic.content = topic_form.content.data
			topic.category_id = topic_form.category_id.data
			topic.tag = topic_form.tag.data

			if topic_form.category_id.data != 0:
				category = Category.get(topic_form.category_id.data)
				category.num += 1

			db_session.add(topic)
		db_session.commit()

		return redirect('/topic/%s' % topic.id)
	else:
		return render_template('/topic/add.html', topic_form=topic_form)


# @topic_page.route('/topic/all')
# def topic_all():
# 	"""
# 	topic all
# 	"""
# 	# topic = Topic.query.all()
# 	tag = TopicTag.query.all()
# 	category = Category.query.all()
#
# 	return render_template('/topic/all.html', tags=tag, categorys=category)
#
#
# #topic=topic)
#
#
# @topic_page.route("/")
# @topic_page.route('/topic/list')
# def topic_list():
# 	"""
# 	topic all
# 	"""
# 	topic = Topic.query.order_by(Topic.id.desc()).all()
# 	# tag = TopicTag.query.all()
# 	category = Category.query.all()
#
# 	return render_template('/topic/list.html',  #tags=tag,
# 	                       category=category, topic=topic)
#
#
# @topic_page.route('/topic/del/<int:id>')
# @login_required
# @is_admin
# def topic_del():
# 	"""
# 	del topic
# 	"""
# 	if id:
# 		Topic.query(Topic.id == id).delete()
# 		return redirect('/')
# 	else:
# 		abort(404)
#
#
# @topic_page.route("/c")
# @topic_page.route("/c/<int:id>")
# def category_show(id=0):
# 	"""
# 	main page
# 	"""
# 	category = Category.query.filter(Category.id == id).first()
# 	# reply_form = ReplyForm()
# 	if category:
# 		return render_template('/topic/category_show.html', category=category)
# 	else:
# 		abort(404)
#
#
# @topic_page.route("/topic/c/add", methods=('get', 'post'))
# @topic_page.route("/topic/c/add/<int:id>", methods=('get', 'post'))
# @login_required
# @is_admin
# def add_category(id=0):
# 	"""
# 	add category
# 	"""
# 	category = Category.query.filter(Category.id == id).first()
# 	category_form = CategoryForm(obj=category)
# 	if request.method == 'POST' and category_form.validate():
# 		if category:
# 			category_form.populate_obj(category)
# 			db_session.flush()
# 			db_session.commit()
# 		else:
# 			category = Category(category_form.name.data)
# 			category.content = category_form.content.data
# 			db_session.add(category)
# 			db_session.flush()
# 			db_session.commit()
# 		return redirect("/c/%s" % category.id)
# 	else:
# 		return render_template('/topic/add_category.html', category_form=category_form)
#
#
# @topic_page.route("/t/id/<int:id>")
# @topic_page.route("/t/name/<string:name>")
# def tag_show(id=0, name=''):
# 	"""
# 	main page
# 	"""
# 	if name is not "":
# 		tag = TopicTag.query.filter(TopicTag.name == name).first()
# 	else:
# 		tag = TopicTag.query.filter(TopicTag.id == id).first()
#
# 	topic_tag = TopicToTag.query.filter(TopicToTag.tag_id == tag.id).all()
# 	tagids = [t.topic_id for t in topic_tag]
# 	topic = Topic.gets(tagids)
#
# 	if tag:
# 		return render_template('/topic/tag_show.html', topic=topic, tag=tag)
# 	else:
# 		abort(404)
