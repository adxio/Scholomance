import urllib2
from sgmllib import SGMLParser

class ListPicName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.urlList = []
	def start_a(self, attrs):
		href = [v for k, v in attrs if k=='href']
		if href:
			self.urlList.append(href)
			print href

def loadUrl(url):
	u = urllib2.urlopen(url)
	content = u.read()
	picList = ListPicName()
	picList.feed(content)
	for pic in picList.urlList:
		pass
		print pic

if __name__ == '__main__':
#	print "input url:"
#	url = raw_input()
	url = "http://www.douban.com/photos/album/51780629/"
	loadUrl(url)
