# -*- coding: utf-8 -*-
import re
from markdown import markdown


def register_jinja_filter(jinja_env):
	jinja_env.filters['string_split'] = string_split
	jinja_env.filters['get_first_pic'] = get_first_pic
	jinja_env.filters['markdown2html'] = markdown2html


def string_split(s, spstr=None):
	if s:
		new_list = s.split(spstr)
	else:
		new_list = []
	return new_list


def get_first_pic(s):
	m = re.search('(?<=<img).+(?=" />)', s)
	if m:
		return m.group(0) + '"'
	else:
		return False


def markdown2html(s, line=0):
	"""
	markdown to html
	s is string
	"""
	html = ''
	if s:
		if line > 0:
			s_list = s.split('\r\n')
			need_cut_s = "\r\n".join(s_list[0:line])
			if need_cut_s.count('<pre><code>') > need_cut_s.count('</code></pre>'):
				need_cut_s += '</code></pre>'

			html = markdown(need_cut_s, ['extra'])
		else:
			html = markdown(s, ['extra'])

	return html