from PIL import Image
import time
import sys

#formatting for the main menu
print("{0:-^50s}".format(''))
print("{0:-^50s}".format('  Main Menu  '))
print("{0:-^50s}".format(''))
print("{0:^50s}".format('Welcome to the CP467 Final Project demo.'))
print()

# gives the user the choice of whether to run the program or end
print("{0:^50s}".format('1. Run demo'))
print("{0:^50s}".format('2. Quit'))

#adds blanks lines and waits for the user input 
print()
menuoption = input('Enter your choice here: ')
print()

# menu option 1 is chosen
if menuoption == "1":
    print("Demo started")
    
    # gets the filename from the user, opens the file, and tells user it imported successfully
    filename = input('Please enter the filename for the image you\'d like to use: ')
    im = Image.open(filename)
    print("Image imported")

# CODE FOR FILTERING GOES HERE
    # High pass filter
    image_width = im.width
    image_height = im.height
    
    for i in range(image_height):
        for j in range(image_width):
            print(im.getpixel((j,i))[0])
# CODE FOR FILTERING GOES HERE
    
    
    # Shows the user the image
    im.show()

# menu option 2 is chosen
elif menuoption == "2":
   
    # exits the program
    print("Quitting program..")
    time.sleep(1.5)
    sys.exit
    
