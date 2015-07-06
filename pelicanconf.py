#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'jack'
SITENAME = "jack's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	     ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )


# Social widget
SOCIAL = (
	      ('Facebook', 'https://www.facebook.com/mini90196'),
          ('Google+', 'https://plus.google.com/u/0/102114822622378471555/posts'),

          )

DEFAULT_PAGINATION = 10

THEME = 'pelican-themes/gum'

DISQUS_SITENAME = "mini90196"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
