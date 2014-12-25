# -*- coding: utf-8 -*-
from flask import Blueprint
from model import db_session, Base
import hashlib


init_page = Blueprint('init_page', __name__)


@init_page.route('/init/create/db')
def create_db():
	"""
	create all db
	"""
	import model.topic
	import model.admin

	# Base.metadata.create_all(engine)
	db_session.create_all()
	return 'create db'


@init_page.route('/init/create/user')
def init_data():
	"""
	init data
	"""
	from model.admin import Admin

	sha1 = hashlib.sha1()
	sha1.update('123456')

	user = Admin("hehehas@gmail.com")
	user.nickname = 'fainle'
	user.password = sha1.hexdigest()

	db_session.add(user)
	db_session.commit()

	return 'update password'