#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
from crawler import booking

urls = ("/", "index")

app = web.application(urls, globals())
render = web.template.render('templates', globals={})

class index:
    def GET(self):
        return render.index()
    def POST(self):
        path = booking.start(str(web.input().url))
        return render.result(path)

if __name__ == "__main__":
    app.run()
