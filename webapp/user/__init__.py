# -*- coding: utf-8 -*-
from functools import wraps
from flask import g, request, redirect, abort, url_for


def login_required(func):
    @wraps(func)
    def _(*args, **kwargs):
        if g.user_id is not None:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user_page.login', next=request.path))

    return _


def is_admin(func):
    @wraps(func)
    def _(*args, **kwargs):
        if g.user_id is not None and g.user_id == 1:
            return func(*args, **kwargs)
        else:
            return abort(404)

    return _