#import numpy
from PIL import Image

myImage = Image.open("grayscale.jpg")
myImage.convert('L')
imgArr = []

height = myImage.height
width = myImage.width

for i in range(height):
	row = []

	for j in range(width):
		row.append(myImage.getpixel((j,i))[0])

	imgArr.append(row)

print(imgArr)