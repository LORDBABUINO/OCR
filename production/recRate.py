from PIL import Image
import subprocess
from padding import *
from filter import *
from thinning import *
from scaling import *
from whiteBlack import *
from multiCharacters import *
from statMethod import *
from database import *
from zsAlgorithm import *
import time
import sys
import copy

def getRecognitionRate():

	total = 0
	correct = 0

	for i in range(0,10):
		for j in range(1, 16):

			try:
				myImage = Image.open("test-nums/{0}_{1}.png".format(i, j)).convert("L")
				print('Image imported successfully')
			except IOError:
				print("Image import failed - file not found")

			myImage = myImage.resize((70,70))
			# Change to BW image
			myImage = convertBW(myImage)
			# Get the unique images
			images = charactersToRead(myImage)

			for image in images:
				original = copy.deepcopy(image)
				image = scaleImage(image, 120, 120)
				image = padZeros(image)
				image = zsAlgorithm(image)
				imageArray = divideImage(image)
				finalCharacter = DBChar(imageArray)
				print("\nThe character in the image is:",finalCharacter,"\n")
				original.show()

				user = input("Correct Input? (y/n) ")

				if user == "y":
					correct += 1
				total += 1

	ratio = correct / total
	print(ratio)
	return

getRecognitionRate()

# p = subprocess.Popen(["/Applications/Preview.app", "test-nums/0_1.png"], shell=True)
# test = input("enter something will")
# p.kill()