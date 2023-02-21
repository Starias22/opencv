import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def read(inputPath):

    """reads an input image file
    Returns:
    numpy.ndarray: the ndarray that represents the image.
    """
    #img reading
    try:
        if inputPath=='':
            raise OSError('Output filename is empty')
        #if the input file doesn't exist
        if not os.path.exists(inputPath):
            raise FileNotFoundError("The input file doesn't exists")
        if os.path.isdir(inputPath):
            raise OSError('The input file is a directory')
        if not os.access(inputPath, os.R_OK):
            raise PermissionError("You don't have reading permission to the specified input path")
        #try to read the image
        img=cv.imread(inputPath )
        #if failure
        if img is None:
            print('Wrong input file')
            #nothing else to do
            #exit()

    except FileNotFoundError as e:
        print(e)
        #exit()
        #return e
    except cv.error as e:
        print('An cv error occured:',e)
        #exit()
    except PermissionError as e:
        print(e)
        #exit()
    except OSError as e:
        print(e)
    except Exception as e:
        print('An error occured:',e)
        #exit()
    else:
        return img

if __name__=='__main__':
    inputPath='../images/apple.jpeg'
    read(inputPath='')#wrong
    read(inputPath='skd')#wrong
    img=read(inputPath='../images/apple.jpeg')
    img=read('../images/apple.jpeg')


    print(img)
    read('/')

