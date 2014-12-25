# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, g
from model import db_session
from webapp.index.view import index_page
from webapp.init.view import init_page
from util.filter import register_jinja_filter


app = Flask(__name__)
app.debug = True


# register blueprint
app.register_blueprint(index_page)
app.register_blueprint(init_page)


# register jijia filter
register_jinja_filter(app.jinja_env)


# error handler
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404


@app.before_request
def before_request():
	"""
	before request
	"""
	if 'is_admin' in session:
		g.is_admin = 1
	else:
		g.is_admin = None


@app.teardown_request
def shutdown_session(exception=None):
	"""
	teardown request
	"""
	db_session.rollback()
	db_session.close()