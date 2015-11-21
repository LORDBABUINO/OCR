from PIL import Image

# Converts an image from grayscale to black and white
def convertBW(myImage):

	for i in range(myImage.width):
		for j in range(myImage.height):
			if myImage.getpixel((j,i)) > 127:
				myImage.putpixel((j,i), 255)
			else:
				myImage.putpixel((j,i), 0)

	return myImage