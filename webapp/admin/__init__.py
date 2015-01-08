# -*- coding: utf-8 -*-
from functools import wraps
from flask import g, request, redirect, url_for


def is_admin(func):
    """
    is admin
    :param func:
    :return:
    """
    @wraps(func)
    def _(*args, **kwargs):
        if g.admin:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin_page.login', next=request.path))

    return _