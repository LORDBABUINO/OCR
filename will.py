import sys
import numpy
from PIL import Image

myImage = Image.open("Lowpass_original.jpg").convert("L")

# Cuts the image given the max/min (x,y) values
def cutImage(myImage, xMin, xMax, yMin, yMax):

	return

def findExtreme(myImage, xSize, ySize, minOrMax, xOrY):

	if minOrMax == "min":
		start = ___ - 1
	elif minOrMax == "max":
		start = 0
	else:
		sys.exit("Input can only be either min or max.")

	# Find the smallest x-value
	myMin = xSize - 1

	for row in range(ySize):
		count = 0
		test = myImage.getpixel((count, row))

		while test != 255:
			count += 1
			test = myImage.getpixel((count, row))

		if count < myMin:
			myMin = count

	return myMin

# Scales the image down to the default size
def scaleImage(myImage, xSize, ySize):



	# Returns the scaled image
	return 

def imgArr(myImage):

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
			row.append(myImage.getpixel((j,i)))

		# Append the row to the main array
		imgArr.append(row)

	return imgArr

# Input:
#	myImage: the padded image to apply the filter to
#	matrix: the matrix to use to multiply the image by
# Output:
#	Filtered image
def applyFilter(myImage, kernel):

	a = 0

	offset = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,0], [0,1], [1,-1], [1,0], [1,1]]

	for i in range(1, myImage.height-1):
		for j in range(1, myImage.width-1):

			for k in range(len(kernel)):
				a += (myImage.getpixel((j+offset[k][0],i+offset[k][1])) * kernel[k])

			myImage.putpixel((j,i), a)


	return myImage

def addPadding(im):
	filtered = Image.new("L", (im.width + 2, im.height + 2), color = 0) #create new image that is 2 pixels wider and taller than the original

	filtered.paste(im, (1, 1), None) #copy image into new image with padding of a 1 pixel border around

	return filtered

kernel = [-1,-1,-1,-1,8,-1,-1,-1,-1]

myImage = addPadding(myImage)

myImage.show()

myImage = applyFilter(myImage, kernel)

myImage.save("test.jpg")
myImage.show()