from PIL import Image

# Converts an image from grayscale to black and white
def convertBW(myImage):

	for i in range(myImage.width):
		for j in range(myImage.height):
			if myImage.getpixel((i,j)) > 0:
				myImage.putpixel((i,j), 255)
			else:
				myImage.putpixel((i,j), 0)

	return myImage

myImage = Image.open("production/test-nums/2_15.png").convert("L")
myImage = convertBW(myImage)
myImage = myImage.resize((70,70))

myImage.show()