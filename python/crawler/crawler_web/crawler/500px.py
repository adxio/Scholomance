#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 500px网站图片爬虫
# 用于收藏自己喜欢的精美图片！请勿商用
# 具体图片使用license请查看500px license(http://500px.com/terms)


import os
import json
import urllib

from threading import Thread
from pyquery import PyQuery as pqr

def download_pic(pic_id, pic_info, pic_idx, page_idx, folder_name):
    global pic_no

    pic_doc = pqr(url="http://500px.com/photo/" + pic_id)
    pic_url =  pqr(pic_doc("div.photo.segment img")).attr("src")
    urllib.urlretrieve(pic_url, folder_name + "/" + pic_id + "." + pic_url.split(".")[-1])
    fileHandle = open(folder_name + "/" + pic_id + ".txt", "w")

    fileHandle.write("info: " + pic_info["info"] + "\n")
    fileHandle.write("title: " + pic_info["title"] + "\n")
    fileHandle.write("rating: " + pic_info["rating"] + "\n")
    fileHandle.close()
    pic_no += 1
    print "Download complete: " + str(pic_idx) + " at Page " + str(page_idx) + ", total: " + str(pic_no)

def scan_page(site_url, folder_name):
    print "Searching pictures at Page " + str(page_no) + " ..."

    folder_name = folder_name + "/" + str(page_no)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    doc = pqr(url=site_url)
    pic_div_list = doc("#px div.container div.d4")
    i = 0

    work_list = []
    for pic in pic_div_list:
        href = pqr(pqr(pic).find("div.photo a")).attr("href")
        pic_id = href.split("/")[-1]
        pic_info = {}
        pic_info["info"] = pqr(pqr(pic).find("div.info a")).text().encode('utf-8')
        pic_info["title"] = pqr(pqr(pic).find("div.title a")).text().encode('utf-8')
        pic_info["rating"] = pqr(pqr(pic).find("div.rating")).text().encode('utf-8')

        i += 1
        worker = Thread(target=download_pic , args=(pic_id, pic_info, i, page_no, folder_name))
        work_list.append(worker)
        worker.start()
    for work in work_list:
        work.join()


if __name__ == '__main__':
    print "Start download"

    global page_no
    global pic_no

    page_no = 0
    pic_no = 0

    query_word = "Sri+Lanka"
    from_idx = 1
    to_idx = 1

    page_no = from_idx - 1

    print "Create folder: " + query_word
    if not os.path.exists(query_word):
        os.mkdir(query_word)

    page_work_list = []

    for page in xrange(from_idx, to_idx + 1):
        page_no += 1
        site_url = "http://500px.com/search?exclude_nude=true&type=photos&page=" + str(page) + "&q=" + query_word
        scan_page(site_url, query_word)
    #     page_work = Thread(target=scan_page , args=(site_url, query_word))
    #     page_work_list.append(page_work)
    #     page_work.start()
    # for page_work in page_work_list:
    #     page_work.join()

    print "Complete!!!"
