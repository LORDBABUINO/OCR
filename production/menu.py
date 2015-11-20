from PIL import Image

def menu ():
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
    print("{0:^50s}".format('4. Getting features'))
    print("{0:^50s}".format('5. Quit'))
    
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
        imgFiltered = applyFilter(imgPadded, kernel)    #filters image
        imgFiltered.show()              #show filtered image
        imgFiltered.save("filteredimage.jpg")
        
    elif menuoption == "2":
        # Gets the file from the user
        filename = input('Please enter the filename for the image you\'d like to use: ')
        
        # Opens file and converts the image to black and white
        imgBase = Image.open(filename).convert("1")
        imgBase.show()
        
        # Thins the image
        imgThinned = thinning(imgBase)
        imgThinned.show()
        print ("done")
    elif menuoption == "3":
        print("opion 3")
    # menu option 3 is chosen
    elif menuoption == "4":
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
    elif menuoption == "5":
        # exits the program
        print("Quitting program..")
        time.sleep(1.5)
        sys.exit