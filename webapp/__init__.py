# -*- coding: utf-8 -*-
from flask import Flask, g, session, render_template
from webapp.main.views import main_page
from webapp.topic.views import topic_page
from webapp.user.views import user_page
#from log.admin.views import admin_page
#from log.topic.views import topic_page
#from log.upload.views import upload_page
from domain import db_session
#from domain.model.user import User
from util.filter import register_jinja_filter


#app config
app = Flask(__name__)
app.config.from_pyfile('setting.ini')
app.config.from_envvar('SETTING', silent=True)


#register blueprint
app.register_blueprint(main_page)
app.register_blueprint(topic_page)
app.register_blueprint(user_page)
#app.register_blueprint(admin_page)
#app.register_blueprint(topic_page)
#app.register_blueprint(upload_page)


#register jijia2 filter
register_jinja_filter(app.jinja_env)


#app before request Category
@app.before_request
def before_request():
    """
    before request
    """
    if 'user_id' in session:
        g.user_id = session['user_id']
        g.nickname = session['nickname']
    else:
        g.user_id = None
        g.nickname = None


#app teardown request
@app.teardown_request
def shutdown_session(exception=None):
    """
    teardown request
    """
    db_session.rollback()
    db_session.close()


@app.route('/google6b4228096abe7a0c.html')
def google_websites():
    """
    google websites
    """
    return render_template('/common/google6b4228096abe7a0c.html')


@app.route('/baidu_verify_Zkeq1VQO9s.html')
def baidu_websites():
    """
    baidu websites
    """
    return render_template('/common/baidu_verify_Zkeq1VQO9s.html')