# -*- coding:utf-8 -*- 
#!/usr/bin/env python

__revision__ = '0.1'
import re
import os
import urllib
import string,time
def get_html_data(url):
    try:
        html=urllib.urlopen(url)
        data=html.read()
    except:
        data=''
    return data
def download_all(urls,dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for url in urls:
        lo="http://img3.douban.com/view/photo/photo/public/p"+url+".jpg" 
        print lo
        base_name=dir+url+".jpg"
        print(base_name)
        urllib.urlretrieve(lo,base_name)
        time.sleep(1)
def get_every_pages(url):
    m=re.compile(r"(?<=http://www.douban.com/photos/photo/)[0-9]*(?=/\")",re.IGNORECASE)
    data=get_html_data(url)
    x=m.findall(data)
    return x
def find_last_page(data):
    m=re.compile(r"(?<=start=)[0-9]*(?=\")")
    list=m.findall(data)
    max=0
    for i in range(len(list)):
        x=string.atoi(list[i])
        if x>max:
            max=x
            
    return max
def check_next_page(data,i):
    m=re.compile(r"start="+str(i),re.S|re.IGNORECASE)
    x=m.findall(data)
    if len(x)==0:
        return False
    else:
        return True
def get_photo(url,dir):
    i=1
    photo_list=[]
    data=get_html_data(url)
    lists=get_every_pages(url)
    photo_list.append(lists)
    last=find_last_page(data)
#    while check_next_page(data,18*i)==True:
    while last-18*i>=0:
        print url+"?start="+str(18*i)
        lists=get_every_pages(url+"?start="+str(18*i))
        #print i
        print last
        photo_list.append(lists)
        i=i+1
    photos=[]
    for p in photo_list:
        if len(p)>1:
            for pp in p:
                photos.append(pp)
        else:
            photos.append(p)
    #print photos
    #print len(photos)
    download_all(photos,dir)
if __name__=="__main__":
    print "input the url:"
    url=raw_input()
    print "input the dir name:"
    dir=raw_input()
    get_photo(url,dir)