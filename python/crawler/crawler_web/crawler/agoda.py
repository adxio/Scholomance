#!/usr/bin/env python
# -*- coding: utf-8 -*-

# booking网站图片爬虫
# 用于收藏自己喜欢的精美图片！请勿商用
# 具体图片使用license请查看500px license(http://500px.com/terms)


import os
import json
import urllib

from threading import Thread
from pyquery import PyQuery as pqr

def download_img(img_url, save_path):
    global img_idx
    global img_cnt

    urllib.urlretrieve(img_url, os.path.join(save_path, img_url.split("/")[-1]))
    img_idx += 1

    if img_idx == img_cnt:
        # os.system("chgrp -R storage %s"%(save_path.encode('utf-8')))
        # os.system("chmod -R 775 %s"%(save_path.encode('utf-8')))
        print "Download all complete: " + save_path.split("/")[-1].encode('utf-8') + "!!!"
    else:
        print "Download %s: %.1f%%" % (save_path.split("/")[-1].encode('utf-8'), float(img_idx)/img_cnt * 100)

def start_download(site_url):
    print "Start download: " + site_url.encode('utf-8')

    global img_idx
    global img_cnt

    img_idx = 0
    img_cnt = 0

    root_path = u"/var/storage/图片收集/booking/"
    # root_path = "/Users/nangua/Desktop/test"

    doc = pqr(url=site_url)

    save_path = os.path.join(root_path, doc("#ctl00_ctl00_MainContent_ContentMain_HotelHeaderHD_lblEHotelName").text()[1:-1])

    print "Create folder: " + save_path.encode('utf-8')

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_list = doc("#ctl00_ctl00_MainContent_ContentMain_MainHotelPhotoHDAB2659_ThumbPhotosHDAB2659_dtlPhotoAB2659 img")
    work_list = []
    img_cnt = len(image_list)
    for img in image_list:
        img_url = pqr(img).attr("src")
        worker = Thread(target=download_img, args=(img_url.replace("_TMB", "_800x600"), save_path))
        work_list.append(worker)
        worker.start()

def get_path(site_url):
    doc = pqr(url=site_url)
    return "booking/" + doc("#hp_hotel_name").text()

def start(site_url):
    worker_main = Thread(target=start_download, args=(site_url,))
    worker_main.start()
    path = get_path(site_url)
    return path
