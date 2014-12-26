# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from model.topic import Topic, Category


index_page = Blueprint('index_page', __name__)


@index_page.before_request
def before_request():
	pass


@index_page.route('/')
@index_page.route('/<int:page>')
def index(page=1):
	"""
	index page
	:param page:
	:return:
	"""
	if page <= 0:
		page = 1

	paginate = Topic.query.paginate(page, 10, False)
	return render_template('/index/index.html', paginate=paginate)


@index_page.teardown_request
def teardown_request(exception):
	pass