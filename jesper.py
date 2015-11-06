from PIL import Image
import time
import sys


print("{0:-^50s}".format(''))
print("{0:-^50s}".format('  Main Menu  '))
print("{0:-^50s}".format(''))
print("{0:^50s}".format('Welcome to the CP467 Final Project demo.'))
print()

print("{0:^50s}".format('1. Run demo'))
print("{0:^50s}".format('2. Quit'))

print()
menuoption = input('Enter your choice here: ')
print()

if menuoption == "1":
    print("Demo started")
    filename = input('Please enter the filename for the image you\'d like to use: ')

    im = Image.open(filename)

    print("Image imported")

// CODE FOR FILTERING GOES HERE
    
    im.show()

elif menuoption == "2":
    print("Quitting program..")
    time.sleep(1.5)
    sys.exit
    
