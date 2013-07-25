#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = (
    '/', 'index'
)

class index(object):
    def GET(self):
        return read_file()

def read_file():
    f = open ("/home/thrall/auth.log")
    file_content = f.read()
    f.close
    return file_content

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
