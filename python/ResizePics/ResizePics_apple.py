import Image, os

def resize(filePath, fileRenamePath, smallFilePath):
	img = Image.open(filePath)
	print smallFilePath
	small_img = img.resize((img.size[0]/2,img.size[1]/2),Image.ANTIALIAS)
	# small_img.save(smallFilePath)
	os.rename(filePath, fileRenamePath)
	small_img.save(filePath)

if __name__ == '__main__':
	print "input path:"
	path = raw_input()
	# path = "/Users/nangua/WORK/git/test"
	fileList = os.listdir(path)
	smallPath = path
	# if not os.path.exists(smallPath): os.makedirs(smallPath)
	for fname in fileList:
		basename, extension = os.path.splitext(fname)
		if extension == ".png":
			resize(path + "/" + fname, path + "/" + basename + "@2x" + extension, smallPath + "/" + fname)
