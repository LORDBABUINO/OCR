#import numpy
import sys
import time
import math
from PIL import Image

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
#    myImage: the padded image to apply the filter to
#    matrix: the matrix to use to multiply the image by
# Output:
#    Filtered image
def applyFilter(img, kernel):
    i = 0
    j = 0
    filtered = Image.new("L", (img.width - 2, img.height - 2))  #create new image

    imageArray = []
    
    for i in range(1, img.width - 1):                        #for every pixel within padding
        for j in range(1, img.height - 1):
            del imageArray[:]                                #clear imageArray each loop
            imageArray.append(img.getpixel((i-1, j-1)))      #populate imageArray with top left pixel
            imageArray.append(img.getpixel((i, j-1)))        #populate imageArray with top middle pixel
            imageArray.append(img.getpixel((i+1, j-1)))      #populate imageArray with top right pixel
            imageArray.append(img.getpixel((i-1, j)))        #populate imageArray with middle left pixel
            imageArray.append(img.getpixel((i, j)))          #populate imageArray with middle pixel
            imageArray.append(img.getpixel((i+1, j)))        #populate imageArray with middle right pixel
            imageArray.append(img.getpixel((i-1, j+1)))      #populate imageArray with bottom left pixel
            imageArray.append(img.getpixel((i, j+1)))        #populate imageArray with bottom middle pixel
            imageArray.append(img.getpixel((i+1, j+1)))      #populate imageArray with bottom right pixel
            filtered.putpixel((i- 1, j- 1), convolute(imageArray, kernel))    #write result of convolution to new image
    return filtered

# Input:
#   imageArray - array containing the 9 pixel grayscale values
#   kernel - kernel matrix used for the convolution
def convolute(imageArray, kernel):
    temp = 0        #used to store current convolution sum
    
    for i in range(0, len(imageArray)):
        temp = temp + (imageArray[i]*kernel[i])    #increment temp by result of image pixel * kernel pixel

    return math.floor(temp)

#contains the 20 rules for thinning.
def thinning(img):
    
    # to identify each pixel 
    # (i-1,j-1)|(i,j-1)|(i+1,j-1)
    #----------------------------
    #  (i-1,j) | (i,j) |(i+1,j)
    #----------------------------
    # (i-1,j+1)|(i,j+1)|(i+1,j+1)
    
    imgA= []        #used to get the pixels around the pixel in question
    
    for i in range(1, img.width - 1):    #for every pixel within padding
        for j in range(1, img.height - 1):
            del imgA[:]        #clear imageArray each loop
            imgA.append(img.getpixel((i-1, j-1)))      #populate imageArray with top left pixel
            imgA.append(img.getpixel((i, j-1)))        #populate imageArray with top middle pixel
            imgA.append(img.getpixel((i+1, j-1)))      #populate imageArray with top right pixel
            imgA.append(img.getpixel((i-1, j)))        #populate imageArray with middle left pixel
            imgA.append(img.getpixel((i, j)))          #populate imageArray with middle pixel
            imgA.append(img.getpixel((i+1, j)))        #populate imageArray with middle right pixel
            imgA.append(img.getpixel((i-1, j+1)))      #populate imageArray with bottom left pixel
            imgA.append(img.getpixel((i, j+1)))        #populate imageArray with bottom middle pixel
            imgA.append(img.getpixel((i+1, j+1)))      #populate imageArray with bottom right pixel
            #rule 1
            if (imgA[0]==1 and imgA[3]==1 and imgA[4]==1 and imgA[6]==1 and imgA[7]==1 and imgA[2]==0 and imgA[5]==0):
                imgA[4] == 0
            
            #rule 2
            elif (imgA[0]==1 and imgA[1]==1 and imgA[3]==1 and imgA[4]==1 and imgA[6]==1 and imgA[5]==0 and imgA[8]==0):
                imgA[4] ==0
            
            #rule 3 
            elif (imgA[0]==1 and imgA[1]==1 and imgA[2]==1 and imgA[4]==1 and imgA[5]==1 and imgA[6]==0 and imgA[7]==0):
                imgA[4] ==0
                
            #rule 4
            elif (imgA[0]==1 and imgA[1]==1 and imgA[2]==1 and imgA[3]==1 and imgA[4]==1 and imgA[7]==0 and imgA[8]==0):
                imgA[4] ==0
            
            #rule 5
            elif (imgA[0]==1 and imgA[3]==1 and imgA[4]==1 and imgA[2]==0 and imgA[5]==0 and imgA[7]==0 and imgA[8]==0):
                imgA[4] ==0
                
            #rule 6 
            elif (imgA[0]==1 and imgA[1]==1 and imgA[4]==1 and imgA[5]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0):
                imgA[4] ==0
                
            #rule 7
            elif (imgA[0]==1 and imgA[1]==1 and imgA[2]==1 and imgA[3]==1 and imgA[4]==1 and imgA[6]==1 and imgA[7]==1 and imgA[8]==1 and imgA[5]==0):
                imgA[4] ==0
                
            #rule 8
            elif (imgA[0]==1 and imgA[1]==1 and imgA[2]==1 and imgA[3]==1 and imgA[4]==1 and imgA[5]==1 and imgA[6]==1 and imgA[8]==1 and imgA[7]==0):
                imgA[4] ==0 
                
            #rule 9
            elif (imgA[3]==1 and imgA[4]==1 and imgA[6]==1 and imgA[1]==0 and imgA[2]==0 and imgA[5]==0 and imgA[8]==0):
                imgA[4] ==0
                
            #rule 10
            elif (imgA[4]==1 and imgA[6]==1 and imgA[7]==1 and imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[5]==0):
                imgA[4] ==0
            #rule 11
            elif (imgA[1]==1 and imgA[2]==1 and imgA[4]==1 and imgA[3]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0):
                imgA[4] == 0
            
            #rule 12
            elif (imgA[2]==1 and imgA[4]==1 and imgA[5]==1 and imgA[0]==0 and imgA[3]==0 and imgA[6]==0 and imgA[7]==0):
                imgA[4] ==0
            
            #rule 13 
            elif (imgA[4]==1 and imgA[7]==1 and imgA[8]==1 and imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[3]==0):
                imgA[4] ==0
                
            #rule 14
            elif (imgA[4]==1 and imgA[5]==1 and imgA[8]==1 and imgA[0]==0 and imgA[1]==0 and imgA[3]==0 and imgA[6]==0):
                imgA[4] ==0
            
            #rule 15
            elif (imgA[0]==1 and imgA[1]==1 and imgA[2]==1 and imgA[4]==1 and imgA[5]==1 and imgA[6]==1 and imgA[7]==1 and imgA[8]==1 and imgA[3]==0):
                imgA[4] ==0
                
            #rule 16 
            elif (imgA[0]==1 and imgA[2]==1 and imgA[3]==1 and imgA[4]==1 and imgA[5]==1 and imgA[6]==1 and imgA[7]==1 and imgA[8]==1 and imgA[1]==0):
                imgA[4] ==0
                
            #rule 17
            elif (imgA[2]==1 and imgA[4]==1 and imgA[5]==1 and imgA[7]==1 and imgA[8]==1 and imgA[0]==0 and imgA[3]==0):
                imgA[4] ==0
                
            #rule 18
            elif (imgA[1]==1 and imgA[2]==1 and imgA[4]==1 and imgA[5]==1 and imgA[8]==1 and imgA[3]==0 and imgA[6]==0):
                imgA[4] ==0 
                
            #rule 19
            elif (imgA[4]==1 and imgA[5]==1 and imgA[6]==1 and imgA[7]==1 and imgA[8]==1 and imgA[0]==0 and imgA[1]==0):
                imgA[4] ==0
                
            #rule 20
            elif (imgA[3]==1 and imgA[4]==1 and imgA[6]==1 and imgA[7]==1 and imgA[8]==1 and imgA[1]==0 and imgA[2]==0):
                imgA[4] ==0
    
    return 
    
def padImage(img):
    padded = Image.new("L", (img.width + 2, img.height + 2), color = 0) #create new image
    i = 0       #counter
    j = 0       #counter
    for i in range(0, padded.width):
        for j in range(0, padded.height):
            #top left
            if (i == 0 and j == 0):
                padded.putpixel((i, j), img.getpixel((i, j)))   #pad top left pixel of padded image with top left pixel of original image
            #top right
            elif (i == padded.width-1 and j == 0):    
                padded.putpixel((i, j), img.getpixel((img.width-1, j)))   #pad top right pixel of padded image with top right pixel of original image
            #bottom left
            elif (i == 0 and j == padded.height-1):
                padded.putpixel((i, j), img.getpixel((i, img.height-1)))   #pad bottom left pixel of padded image with top right pixel of original image
            #bottom right
            elif (i == padded.width-1 and j == padded.height-1):
                padded.putpixel((i, j), img.getpixel((img.width-1, img.height-1)))   #pad bottom right pixel of padded image with top right pixel of original image
            #left side
            elif (i == 0):
                padded.putpixel((i, j), img.getpixel((i, j-1))) #pad left side of padded image with pixels along left side of original image
            #right side
            elif (i == padded.width-1):
                padded.putpixel((i, j), img.getpixel((img.width-1, j-1)))   #pad right side of padded image with pixels along right side of original image
            #top side
            elif (j == 0):
                padded.putpixel((i, j), img.getpixel((i-1, j)))     #pad top side of padded image with pixels along top side of original image
            #bottom side
            elif (j == padded.height-1):
                padded.putpixel((i, j), img.getpixel((i-1, img.height-1)))      #pad bottom side of padded image with pixels along bottom side of original image
            #inside pixels
            else:
                padded.putpixel((i, j), img.getpixel((i-1, j-1)))       #pad the rest of the padded image with the pixels from the rest of the original image
    return padded

def main ():
    #formatting for the main menu
    print("{0:-^50s}".format(''))
    print("{0:-^50s}".format('  Main Menu  '))
    print("{0:-^50s}".format(''))
    print("{0:^50s}".format('Welcome to the CP467 Final Project demo.'))
    print()
    
    # gives the user the choice of whether to run the program or end
    print("{0:^50s}".format('1. Filtering'))
    print("{0:^50s}".format('2. Thinning'))
    print("{0:^50s}".format('3. Scaling'))
    print("{0:^50s}".format('4. Quit'))
    
    #adds blanks lines and waits for the user input 
    print()
    menuoption = input('Enter your choice here: ')
    print()
    
    # menu option 1 is chosen
    if menuoption == "1":
        
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
    
        print("{0:-^50s}".format(''))
        print("{0:-^50s}".format('  Select your Filter  '))
        print("{0:-^50s}".format(''))
        print("{0:^50s}".format('1. High Pass Filter'))
        print("{0:^50s}".format('2. Low Pass Filter'))
        filteroption = input('Enter your choice here: ')

        if filteroption == "1":
            kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
        elif filteroption == "2":
            kernel = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
        #end if
        imgBase.show()        
        imgPadded = padImage(imgBase) #pad input image
        imgPadded.show()
#        imgFiltered = applyFilter(imgPadded, kernel)    #filters image
#        imgFiltered.show()              #show filtered image
#        imgFiltered.save("filteredimage.jpg")
        
    elif menuoption == "2":
        print("option 2")
    elif menuoption == "3":
        print("opion 3")
    # menu option 2 is chosen
    elif menuoption == "4":
        # exits the program
        print("Quitting program..")
        time.sleep(1.5)
        sys.exit
        
main()
