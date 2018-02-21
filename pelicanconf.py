#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CEE'
SITENAME = u'insights-core-blog'
SITEURL = 'https://redhatinsights.github.io/insights-core-blog'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = "./themes/gum"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = "https://github.com/RedHatInsights/insights-core-blog"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
