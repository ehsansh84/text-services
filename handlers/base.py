#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
__author__ = 'Ehsan'


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('base.html')


class PostTextHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Your text has been posted')


class GetTextHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('You get this text!')
