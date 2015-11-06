from PIL import Image
import time
import sys

def kernel_matrix():
    kerArr = [-1,-1,-1,-1,8,-1,-1,-1,-1]
    return kerArr

def imgfilter(im,kernel):
    
    ker = kernel
    
    # Get height and width values
    height = im.height
    width = im.width

    for i in range(1,width):
        for j in range(1,height):
                    a = im.getpixel((i,j))[0]
                    temp = (ker[0]*(im.getpixel((i-1,j-1))[0]))+(ker[1]*(im.getpixel((i,j-1))[0]))+(ker[2]*(im.getpixel((i+1,j-1))[0]))
                    temp1 = (ker[3]*(im.getpixel((i-1,j))[0]))+(ker[4]*(im.getpixel((i,j))[0]))+(ker[5]*(im.getpixel((i+1,j))[0]))
                    temp2 = (ker[6]*(im.getpixel((i-1,j+1))[0]))+(ker[7]*(im.getpixel((i,j+1))[0]))+(ker[8]*(im.getpixel((i+1,j+1))[0]))
                    b = temp+temp1+temp2
                    
    return 

def applyFilter(myImage, kernel):

    a = 0

    offset = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,0], [0,1], [1,-1], [1,0], [1,1]]

    for i in range(1, myImage.height-1):
        for j in range(1, myImage.width-1):

            for k in range(len(kernel)):
                a += (myImage.getpixel((j+offset[k][0],i+offset[k][1])) * kernel[k])

            myImage.putpixel((j,i), a)


    return myImage



def padding(im):
    padded = Image.new("L", (im.width + 2, im.height + 2), color = 0) #create new image that is 2 pixels wider and taller than the original

    padded.paste(im, (1, 1), None) #copy image into new image with padding of a 1 pixel border around

    padded.show()
    return padded

    
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
    
    img = padding(im)
    myImage = applyfilter(img,kernel_matrix())
# CODE FOR FILTERING GOES HERE
    
    # Shows the user the image
    myImage.show()

# menu option 2 is chosen
elif menuoption == "2":
   
    # exits the program
    print("Quitting program..")
    time.sleep(1.5)
    sys.exit