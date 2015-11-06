# ------------------------------------------------------------------
# CP467 Image Processing Demo
# Friday November 6 2015
# ------------------------------------------------------------------

from PIL import Image        #our demo uses the Pillow library for importing images
import time                  #used to add pauses in execution
import sys                   #used to close program if user decides to quit

#PRINTING MAIN MENU
print("{0:-^50s}".format(''))
print("{0:-^50s}".format('  Main Menu  '))
print("{0:-^50s}".format(''))
print("{0:^50s}".format('Welcome to the CP467 Final Project demo.'))
print()

print("{0:^50s}".format('1. Run demo'))
print("{0:^50s}".format('2. Quit'))


print()
menuoption = input('Enter your choice here: ')        #gets input from user
print()

if menuoption == "1":            #user decided to run demo
    print("Demo started")
    filename = input('Please enter the filename for the image you\'d like to use: ')    #get image filename from user

    im = Image.open(filename)    #import user-specified image

    print("Image imported")      #status message

// CODE FOR FILTERING GOES HERE
    
    im.show()                    #show image after filter

elif menuoption == "2":            #user decided to close the program
    print("Quitting program..")    #display message to inform user that they're quitting the program
    time.sleep(1.5)                #close after 1.5 seconds
    sys.exit
    
