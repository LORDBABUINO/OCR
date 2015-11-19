import sys
import numpy
from PIL import Image

#myImage = Image.open("testing2.jpg").convert("L")

myImage = Image.new("L", (90,90), color=255)

myImage.putpixel((40,45), 65)
myImage.putpixel((60,50), 65)

def check(minOrMax, count, start):

	if minOrMax == "min":
		return count < start
	else:
		return count > start

def findExtreme(myImage, minOrMax, xOrY):

	xSize = myImage.size[0]
	ySize = myImage.size[1]

	if xOrY == "x":
		outside = xSize
		inside = ySize
	elif xOrY == "y":
		outside = ySize
		inside = xSize
	else:
		sys.exit("Input can only be either x or y.")

	if minOrMax == "min":
		start = outside - 1
		end = 0
	elif minOrMax == "max":
		start = 0
		end = outside - 1
	else:
		sys.exit("Input can only be either min or max.")

	# Find the smallest x-value
	myVal = start

	for row in range(inside):
		count = end

		if xOrY == "x":
			test = myImage.getpixel((count, row))
		else:
			test = myImage.getpixel((row, count))

		while test == 255 and check(minOrMax, count, start):
			
			if minOrMax == "min":
				count += 1
			else:
				count -= 1
			
			if xOrY == "x":
				test = myImage.getpixel((count, row))
			else:
				test = myImage.getpixel((row, count))
		
		if minOrMax == "min":
			if count < myVal:
				myVal = count
		else:
			if count > myVal:
				myVal = count

	return myVal

# Scales the image down to the default size
def scaleImage(myImage, width, height):

	xMin = findExtreme(myImage, "min", "x")
	xMax = findExtreme(myImage, "max", "x")
	yMin = findExtreme(myImage, "min", "y")
	yMax = findExtreme(myImage, "max", "y")

	print("xMin:", xMin, "xMax:", xMax)
	print("yMin:", yMin, "yMax:", yMax)

	myImage = myImage.crop((xMin, yMin, xMax+1, yMax+1))

	# Resizes the image to the given width x height
	myImage = myImage.resize((width,height))

	# Returns the scaled image
	return myImage

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

myImage = scaleImage(myImage, 120, 120)

myImage.show()
