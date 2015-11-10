from PIL import Image
from PIL import ImageFilter

baseIMG = Image.open("dog.jpg").convert("L")

def applyFilter(img, kernel):
    i = 0        # initialize counter
    j = 0
    filtered = Image.new("L", (img.width - 2, img.height - 2))  #create new image 

    imageArray = []        #used to pass pixels to convolution function
    
    for i in range(1, img.width - 1):    #for every pixel within padding
        for j in range(1, img.height - 1):
            del imageArray[:]        #clear imageArray each loop
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

def padImage(img):
    padded = Image.new("L", (img.width + 2, img.height + 2), color = 0) #create new image

    padded.paste(img, (1, 1), None)     #copy image into new image with padding

    return padded

def convolute(image, kernel):
    temp = 0        #used to store current convolution sum
    
    for i in range(0, len(image)):
        temp = temp + (image[i]*kernel[i])    #increment temp by result of image pixel * kernel pixel

    return temp
    
kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]    #high pass filter
padIMG = padImage(baseIMG)        #pad image with 0's
filterIMG = applyFilter(padIMG, kernel)    #filter image with kernel
filterIMG.save("output.jpg")        #save new image with filename "output.jpg"
