import numpy
from PIL import Image

myImage = Image.open("Lowpass_original.jpg").convert("L")

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

print(myImage.size)

myImage = addPadding(myImage)

myImage.show()

print(imgArr(myImage))

print(myImage.size)

myImage = applyFilter(myImage, kernel)

print(imgArr(myImage))

myImage.save("test.jpg")
myImage.show()