#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
from crawler import booking

urls = (
    "/", "index",
    "/log", "log"
    )

app = web.application(urls, globals())
render = web.template.render('templates', globals={})

class index:
    def GET(self):
        return render.index()
    def POST(self):
        path = booking.start(str(web.input().url))
        return render.result(path)

class log:
    def GET(self):
        f = open("crawler.log")
        logs = []
        line = f.readline()
        while line:
            if not line.startswith("192"):
                logs.append(line)
            line = f.readline()

        f.close()
        ret = ["..."]
        ret.extend(logs[-15:])
        return render.log(ret)

if __name__ == "__main__":
    app.run()
