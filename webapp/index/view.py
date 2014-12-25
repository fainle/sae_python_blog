# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from model.topic import Topic, Category


index_page = Blueprint('index_page', __name__)


@index_page.before_request
def before_request():
	pass


@index_page.route('/')
def index():
	topic = Topic.query.order_by(Topic.id.desc()).all()
	category = Category.query.all()
	return render_template('/index/index.html', category=category, topic=topic)


@index_page.teardown_request
def teardown_request(exception):
	pass