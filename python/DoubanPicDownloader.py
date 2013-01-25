import urllib2
from sgmllib import SGMLParser

class ListPicName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_img = 0
		self.urlList = []
	def start_img(self, attrs):
		self.is_img = 1
	def end_img(self):
		self.is_img = 0
	def handle_data(self, text):
		if self.is_img == 1:
			print text
			self.urlList.append(text)

def loadUrl(url):
	u = urllib2.urlopen(url)
	content = u.read()
	picList = ListPicName()
	picList.feed(content)
	for pic in picList.urlList:
		pass
#		print pic

if __name__ == '__main__':
#	print "input url:"
#	url = raw_input()
	url = "http://www.douban.com/photos/photo/1852669569/"
	loadUrl(url)