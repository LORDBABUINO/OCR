#import numpy
from PIL import Image

myImage = Image.open("grayscale.jpg")
myImage.convert('L')

def imgArr(original):

	# Create array of image values
	imgArr = []

	# Get height and width values
	height = myImage.height
	width = myImage.width

	# Get all rows
	for i in range(height):
		row = []

		# Add each value to the row
		for j in range(width):
			row.append(myImage.getpixel((j,i))[0])

		# Append the row to the main array
		imgArr.append(row)

	return imgArr