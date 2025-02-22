#import face_recognition
import cv2
import numpy as np
import os


path = 'ImagesAttendance'
images = []     # LIST CONTAINING ALL THE IMAGES
studName = []    # LIST CONTAINING ALL THE CORRESPONDING student Names

def getImages():
    '''listdir(path)  from the os module returns a list containing the names of the entries in a directory.
    It basically fetches all the files and directories present in the specified path and
    returns them as a list of strings. '''
    myList = os.listdir(path)
    print(type(myList))
    print("mylist", myList)
    print("Total Classes Detected:",len(myList))

    '''The enumerate() function in Python is used to loop over an iterable (ex. list, tuple, string)
    while also keeping track of the index of the current item.
    It returns a tuple for each element in the list. The tuple contains two values:
    the index of the element and the element itself.'''
    studNum=0
    for num, ele in enumerate(myList):
        print("ele is : ", ele)

        '''splitting the read filename to check if it has an jpeg extn. Doing this because.
        there is a file called thumb.db by default in the directory and program crashes
        everytime this file is read.'''
        parts = ele.split('.')
        if (parts[1] == 'jpeg'):
            curImg = cv2.imread(f'{path}/{ele}')    #read the image
            images.append(curImg)
            studName.append(parts[0])        
        else:
            continue
    return images,studName  
    #Now images contains the photos of the students. Comment this after debugging. 
'''   n=0
    
    for n, img in enumerate(images):
        print("image num: ", n)
        cv2.imshow("rez_img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("type of return value is :", type(images))'''
    
    
