#coding=UTF8
import os
import string

path = os.getcwd()

if not os.path.exists(path):
	print "Path not exist!"
else:
	for root, dirs, files in os.walk(path):
		for name in files:
			if name == '.DS_Store':
				continue
			if name.startswith("最完美"):
				old_full_name = os.path.join(root, name)
				new_name = name[37:40] + name
				new_full_name = os.path.join(root, new_name)
				print new_name
				os.rename(old_full_name, new_full_name)
print 'Rename all done!'
