#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base

__author__ = 'Ehsan'

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/get_text", base.GetTextHandler, None, "index"),
    ("/post_text", base.PostTextHandler, None, "index"),
]
