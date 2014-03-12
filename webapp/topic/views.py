__author__ = 'apple'
from flask import Blueprint, render_template, g, abort, request, redirect
from domain import db_session
from domain.model.topic import Topic, Category, TopicTag, TopicToTag
from webapp.topic.forms import TopicForm


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


@topic_page.route('/topic/add', methods=("POST", "GET"))
@topic_page.route('/topic/add/<int:id>', methods=("POST", "GET"))
#@login_required
#@is_admin
def topic_add(id=0):
    topic = Topic.query.filter(Topic.id == id).first()
    topic_form = TopicForm(obj=topic)
    topic_form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by(Category.id.asc()).all()]
    if request.method == 'POST' and topic_form.validate():
        if topic:
            if topic.category_id != topic_form.category_id.data:
                new_category = Category.get(topic_form.category_id.data)
                new_category.num += 1
                old_category = Category.get(topic.category_id)
                old_category.num -= 1

            tag_list = topic_form.tag.data.split(" ")
            for tag_name in tag_list:
                if tag_name.strip():
                    tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
                    if tag:
                        topic_to_tag = TopicToTag.query.filter(TopicToTag.topic_id == id).filter(
                            TopicToTag.tag_id == tag.id).first()
                        if topic_to_tag is None:
                            tag.num += 1
                            topic_to_tag = TopicToTag(id, tag.id)
                            db_session.add(topic_to_tag)
                    else:
                        tag = TopicTag(tag_name)
                        db_session.add(tag)
                        db_session.flush()
                        topic_to_tag = TopicToTag(topic.id, tag.id)
                        db_session.add(topic_to_tag)

            topic_form.populate_obj(topic)
            db_session.commit()
        else:
            topic = Topic(topic_form.title.data)
            topic.content = topic_form.content.data
            topic.category_id = topic_form.category_id.data
            topic.tag = topic_form.tag.data
            db_session.add(topic)
            db_session.flush()

            category = Category.get(topic_form.category_id.data)
            category.num += 1
            tag_list = topic_form.tag.data.split(" ")
            for tag_name in tag_list:
                if tag_name.strip():
                    tag = TopicTag.query.filter(TopicTag.name == tag_name).first()
                    if tag:
                        tag.num += 1
                    else:
                        tag = TopicTag(tag_name)
                        db_session.add(tag)
                        db_session.flush()
                    topic_to_tag = TopicToTag(topic.id, tag.id)
                    db_session.add(topic_to_tag)
            db_session.commit()
        return redirect('/')
    else:
        return render_template('/topic/add.html',
                               topic_form=topic_form,
        )