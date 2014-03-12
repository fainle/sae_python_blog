from flask import Blueprint, render_template, abort
from domain import db_session, engine
from domain.model import Base
from domain.model.topic import Topic
import hashlib


main_page = Blueprint('main_page', __name__)


@main_page.route("/")
def main():
    """
    main page
    """
    topic = Topic.query.filter(Topic.id == 1).first()
    #reply_form = ReplyForm()
    if topic:
        #category = Category.query.filter(Category.id == topic.category_id).first()
        #reply = TopicReply.query.filter(TopicReply.topic_id == topic.id).all()
        topic.count.views += 1
        db_session.commit()
    else:
        abort(404)

    return render_template('/topic/show.html',
                           topic=topic)
                           #category=category,
                           #count=topic.count,
                           #reply_form=reply_form,
                           #reply=reply,)


@main_page.route("/test")
@main_page.route("/test.html")
def test():
    """
    test
    """
    return render_template('test.html')


@main_page.route('/db/create/db')
def create_db():
    """
    create all db
    """

    from domain.model.user import User
    from domain.model.topic import Topic, Category, TopicTag, TopicCount, TopicToTag

    Base.metadata.create_all(engine)

    return 'create db'


@main_page.route('/db/create/user')
def init_data():
    """
    init data
    """
    from domain.model.user import User

    sha1 = hashlib.sha1()
    sha1.update('123456')

    user = User("hehehas@gmail.com")
    user.nickname = 'fainle'
    user.password = sha1.hexdigest()

    db_session.add(user)
    db_session.commit()