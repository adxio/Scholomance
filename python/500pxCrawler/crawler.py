#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 500px网站图片爬虫
# 用于收藏自己喜欢的精美图片！请勿商用
# 具体图片使用license请查看500px license(http://500px.com/terms)


import os
import json
import urllib
from pyquery import PyQuery as pqr

def download_pic(pic_id, pic_info, query_word):
    pic_doc = pqr(url="http://500px.com/photo/" + pic_id)
    pic_url =  pqr(pic_doc("div.photo.segment img")).attr("src")
    urllib.urlretrieve(pic_url, query_word + "/" + pic_id + "." + pic_url.split(".")[-1])
    fileHandle = open(query_word + "/" + pic_id + ".txt", "w")

    fileHandle.write("info: " + pic_info["info"] + "\n")
    fileHandle.write("title: " + pic_info["title"] + "\n")
    fileHandle.write("rating: " + pic_info["rating"] + "\n")
    fileHandle.close()

def scan_page(site_url, query_word):
    global page_no
    global pic_no
    print "Searching pictures at Page " + str(page_no) + " ..."

    doc = pqr(url=site_url)
    pic_div_list = doc("#px div.container div.d4")
    for pic in pic_div_list:
        href = pqr(pqr(pic).find("div.photo a")).attr("href")
        pic_id = href.split("/")[-1]
        pic_info = {}
        pic_info["info"] = pqr(pqr(pic).find("div.info a")).text()
        pic_info["title"] = pqr(pqr(pic).find("div.title a")).text()
        pic_info["rating"] = pqr(pqr(pic).find("div.rating")).text()

        pic_no += 1
        print "Downloading ..."
        download_pic(pic_id, pic_info, query_word)
        print "Download complete: " + str(pic_no) + " at Page " + str(page_no)

if __name__ == '__main__':
    print "Start download"

    global page_no
    global pic_no

    page_no = 0
    pic_no = 0

    query_word = "Sri+Lanka"
    from_idx = 1
    to_idx = 827

    print "Create folder: " + query_word
    if not os.path.exists(query_word):
        os.mkdir(query_word)

    for page in xrange(from_idx, to_idx + 1):
        page_no += 1
        site_url = "http://500px.com/search?exclude_nude=true&type=photos&page=" + str(page) + "&q=" + query_word
        scan_page(site_url, query_word)
