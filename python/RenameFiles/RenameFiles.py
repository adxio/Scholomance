#coding=UTF8
import os
import string


path = raw_input("Input the path:")
if '' == path:
	path = os.getcwd()
print "path:" + path
if not os.path.exists(path):
	print "Path not exist!"
else:
	for root, dirs, files in os.walk(path):
		for pre_name in files:
			if pre_name == '.DS_Store':
				continue
			if pre_name.startswith("[电影天堂www.dy2018.net]"):
				pre_full_name = os.path.join(root, pre_name)
				new_full_name = os.path.join(root, pre_name[28:])
				print new_full_name
				os.rename(pre_full_name, new_full_name)
print 'Rename all done!'
