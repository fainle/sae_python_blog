# -*- coding: utf-8 -*-
from flask import Blueprint
from model import db_session, db
from hashlib import sha1


init_page = Blueprint('init_page', __name__)


@init_page.route('/init/create/db')
def create_db():
	"""
	create all db
	"""
	import model.topic
	import model.admin

	db.create_all()
	return 'create db'


@init_page.route('/init/create/user')
def init_data():
	"""
	init data
	"""
	from model.admin import Admin

	user = Admin("hehehas@gmail.com")
	user.password = sha1('123456').hexdigest()

	db_session.add(user)
	db_session.commit()

	return 'update password'