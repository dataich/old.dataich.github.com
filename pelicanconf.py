#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '.'

AUTHOR = 'dataich'
SITENAME = "Cap'n webb"
SITEURL = 'http://blog.dataich.com'
#SITEURL = 'http://localhost:8000'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
DEFAULT_PAGINATION = False
DEFAULT_DATE_FORMAT = '%Y/%m/%d'
SUMMARY_MAX_LENGTH = 0

DISQUS_SITENAME = 'capnwebb'
GOOGLE_ANALYTICS = 'UA-2954918-13'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*).*'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL + '/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = CATEGORY_URL + '/index.html'
ARCHIVES_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
TAGS_SAVE_AS = False

THEME = 'pelican-themes/pelican-cait'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
	('Contact', 'contact'),
	('Dicstory', 'dicstory'),
	('LiveDiag', 'LiveDiag')
)
CONTACT_EMAIL = "taichiro.yoshida@gmail.com"
CONTACTS = (
	('facebook', 'https://www.facebook.com/dataich'),
	('twitter', 'https://twitter.com/dataich'),
	('github', 'https://github.com/dataich'),
)
