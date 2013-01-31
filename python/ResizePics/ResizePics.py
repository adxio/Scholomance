import Image, os

def resize(filePath,smallFilePath):
	img = Image.open(filePath)
	print smallFilePath
	small_img = img.resize((80,70),Image.ANTIALIAS)
	small_img.save(smallFilePath)

if __name__ == '__main__':
	print "input path:"
	path = raw_input()
	fileList = os.listdir(path)
	for fname in fileList:
		basename, extension = os.path.splitext(fname)
		if extension == ".png":
			resize(path + "/" + fname, path + "/small/" + fname)
