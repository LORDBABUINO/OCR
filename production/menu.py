from PIL import Image
from padding import *
from filter import *
from thinning import *
from scaling import *
from whiteBlack import *
from multiCharacters import *
from statMethod import *
import time
import sys

def menu ():
    while True:
        #formatting for the main menu
        print("{0:-^50s}".format(''))
        print("{0:-^50s}".format('  Main Menu  '))
        print("{0:-^50s}".format(''))
        print("{0:^50s}".format('Welcome to the CP467 Final Project demo.'))
        print()
        
        # gives the user the choice of whether to run the program or end
        print("{0:^50s}".format('1. OCR System'))
        print("{0:^50s}".format('2. Filtering'))
        print("{0:^50s}".format('3. Thinning'))
        print("{0:^50s}".format('4. Scaling'))
        print("{0:^50s}".format('5. Getting features'))
        print("{0:^50s}".format('6. Quit'))
        
        #adds blanks lines and waits for the user input 
        print()
        menuoption = input('Enter your choice here: ')
        print()
        
        if menuoption == "1":

            while True:
                # gets the filename from the user, opens the file, and tells user it imported successfully
                filename = input('Please enter the filename for the image you\'d like to use: ')

                try:
                    myImage = Image.open(filename).convert("L")
                    print('')
                    print('Image imported successfully')
                    print('')
                    break
                except IOError:
                    print("Image import failed - file not found")

            myImage = myImage.resize((160,160))

            # Pad the image    
            myImage = padImage(myImage) 
            
            # Apply high pass filter to the image
            kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
            myImage = applyFilter(myImage, kernel)

            # Apply low pass filter to the image
            kernel = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
            myImage = applyFilter(myImage, kernel)

            myImage.show()

            # Change to BW image
            myImage = convertBW(myImage)

            myImage.show()

            # Invert white/black pixels
            myImage = invert(myImage)

            myImage.show()

            # Get the unique images
            images = charactersToRead(myImage)
            count = 0

            for image in images:
                image = scaleImage(image, 120, 120)
                image.show()
                image = thinning(image)
                image.show()
                imageArray = divideImage(image)
                print(imageArray)


        elif menuoption == "2":
            
            while True:
                # gets the filename from the user, opens the file, and tells user it imported successfully
                filename = input('Please enter the filename for the image you\'d like to use: ')

                try:
                    imgBase = Image.open(filename).convert("L")
                    print('')
                    print('Image imported successfully')
                    print('')
                    break
                except IOError:
                    print("Image import failed - file not found")
            
            while True:

                print("{0:-^50s}".format(''))
                print("{0:-^50s}".format('  Select your Filter  '))
                print("{0:-^50s}".format(''))
                print("{0:^50s}".format('1. High Pass Filter'))
                print("{0:^50s}".format('2. Low Pass Filter'))

                print()
                filteroption = input('Enter your choice here: ')
                print()

                if filteroption == "1":
                    kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
                    break
                elif filteroption == "2":
                    kernel = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
                    break
                else:
                    print("Invalid option. Please try again.\n")
            #end if
            imgBase.show()        
            imgPadded = padImage(imgBase) #pad input image
            imgFiltered = applyFilter(imgPadded, kernel)    #filters image
            imgFiltered.show()              #show filtered image
            
        elif menuoption == "3":

            while True:
                # Gets the file from the user
                filename = input('Please enter the filename for the image you\'d like to use: ')
                
                try:
                    # Opens file and converts the image to black and white
                    imgBase = Image.open(filename).convert("1")
                    imgBase.show()
                    
                    # Thins the image
                    t1=time.time()
                    imgThinned = thinning(imgBase)
                    print(time.time()-t1)
                    imgThinned.show()

                    print("\nComplete.\n")
                    break
                except IOError:
                    print("Image import failed - file not found")

        elif menuoption == "4":

            while True:
                # Gets the file from the user
                filename = input('Please enter the filename for the image you\'d like to use: ')
                
                try:
                    # Opens file and converts the image to grayscale
                    imgBase = Image.open(filename).convert("L")
                    imgBase.show()
                    
                    # Thins the image
                    imgThinned = scaleImage(imgBase, 120, 120)
                    imgThinned.show()

                    print("\nComplete.\n")
                    break
                except IOError:
                    print("Image import failed - file not found")

        elif menuoption == "5":
            print("Getting features")
            while True:
                # gets the filename from the user, opens the file, and tells user it imported successfully
                filename = input('Please enter the filename for the image you\'d like to use: ')

                try:
                    imgBase = Image.open(filename).convert("L")
                    print('')
                    print('Image imported successfully')
                    print('')
                    break
                except IOError:
                    print("Image import failed - file not found")

            print(divideImage(imgBase))
        elif menuoption == "6":
            # exits the program
            print("Quitting program.\n")
            break
        else:
            print()
            print("Not a valid menu option. Please try again.")
            print()
