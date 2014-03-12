# -*- coding: utf-8 -*-
import re

def register_jinja_filter(jinja_env):

	jinja_env.filters['string_split'] = string_split
	jinja_env.filters['get_first_pic'] = get_first_pic


def string_split(s, spstr=None):
	if s:
		new_list = s.split(spstr)
	else:
		new_list = []
	return new_list


def get_first_pic(s):
	m = re.search('(?<=<img).+(?=" />)',s)
	if m:
		return m.group(0)+'"'
	else:
		return False	