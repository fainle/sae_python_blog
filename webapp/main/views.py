from flask import Blueprint, render_template

main_page = Blueprint('main_page', __name__)


@main_page.route("/")
def main():
    """
    main page
    """
    return render_template('login.html')


@main_page.route("/test")
@main_page.route("/test.html")
def test():
    """
    test
    """
    return render_template('test.html')