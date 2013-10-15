from flask import Blueprint, render_template

main_page = Blueprint('main_page', __name__)

@main_page.route("/")
def main():
	return render_template('index.html')