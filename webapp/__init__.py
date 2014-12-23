# -*- coding: utf-8 -*-
from flask import Flask, render_template
from webapp.index.view import index_page


app = Flask(__name__)
app.debug = True


# register blueprint
app.register_blueprint(index_page)


# error handler
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404