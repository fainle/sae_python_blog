__author__ = 'apple'
from flask import Blueprint, render_template, g, abort
from domain import db_session
from domain.model.topic import Topic


topic_page = Blueprint('topic_page', __name__)


@topic_page.route("/<int:id>")
def topic_show(id=0):
    """
    main page
    """
    topic = Topic.query.filter(Topic.id == id).first()
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