import Image, os

def resize(filePath,smallFilePath):
	img = Image.open(filePath)
	print smallFilePath
	small_img = img.resize((80,70),Image.ANTIALIAS)
	small_img.save(smallFilePath)

if __name__ == '__main__':
	#print "input path:"
	#path = raw_input()
	path = "/Users/nangua/Desktop/logo.iconset"
	img = Image.open(path + "/icon.png")

	img512r = img.resize((1024,1024),Image.ANTIALIAS)
	img512r.save(path + "/icon_512x512@2x.png")

	img512 = img.resize((512,512),Image.ANTIALIAS)
	img512.save(path + "/icon_512x512.png")
	img512.save(path + "/icon_256x256@2x.png")

	img256 = img.resize((256,256),Image.ANTIALIAS)
	img256.save(path + "/icon_256x256.png")
	img256.save(path + "/icon_128x128@2x.png")

	img128 = img.resize((128,128),Image.ANTIALIAS)
	img128.save(path + "/icon_128x128.png")

	img64 = img.resize((64,64),Image.ANTIALIAS)
	img64.save(path + "/icon_32x32@2x.png")

	img32 = img.resize((32,32),Image.ANTIALIAS)
	img32.save(path + "/icon_32x32.png")
	img32.save(path + "/icon_16x16@2x.png")

	img16 = img.resize((16,16),Image.ANTIALIAS)
	img16.save(path + "/icon_16x16.png")

	os.popen("iconutil -c icns " + path)