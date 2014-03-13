# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, g, session, redirect, url_for
from webapp.user.form import LoginForm, RegisterForm
from domain.model.user import User
from domain.model.topic import Category
from domain import db_session
import hashlib


user_page = Blueprint("user_page", __name__)


@user_page.context_processor
def _():
    g.category = Category.query.all()
    return dict(code=200)


@user_page.route("/user/register", methods=('POST', 'GET'))
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST':
        if register_form.validate():
            user = User(register_form.email.data)
            user.nickname = register_form.nickname.data
            sha1 = hashlib.sha1()
            sha1.update(register_form.password.data)
            user.password = sha1.hexdigest()
            db_session.add(user)
            db_session.commit()
            session['user_id'] = user.id
            session['nickname'] = user.nickname
            return redirect(request.args.get('next') or '/user')
    return render_template('/user/register.html',
                           registerform=register_form
    )


@user_page.route("/user/login", methods=("POST", "GET"))
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        if login_form.validate():
            session['user_id'] = login_form.user.id
            session['nickname'] = login_form.user.nickname
            return redirect(request.args.get('next') or '/user')

    return render_template("/user/login.html",
                           loginform=login_form
    )


@user_page.route("/user/logout")
def logout():
    session.pop('user_id', None)
    session.pop('nickname', None)
    return redirect(request.args.get('next') or '/user')


@user_page.route("/user")
def user():
    return render_template('/user/index.html')