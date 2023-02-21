import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'sr', 'ras', 'tiff', 'tif', 'pbm', 'pgm','ppm']
def gray(inputPath,outputPath):
    """converts an image to grayscale

    Args:
        inputPath (str): the path of the input image file
        outputPath (str): the path of the output image file
    """
    #img reading
    try:
        wtb=wrt.iswritable(outputPath)
        if wtb is None:
            return
        #try to read the image
        img=reading.read(inputPath )
        #if failure
        if img is None:
            #nothing else to do
            return
        #else
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        if wt.imwrite(img,outputPath):
            print('Image successfully converted to grayscale:')

    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:')

if __name__=='__main__':
    inputPath='./images/apple.jpeg'
    gray(inputPath='',outputPath='')#wrong
    gray(inputPath='skd',outputPath='wrong')#wrong
    gray(inputPath='../src/images/apple.jpeg',outputPath='xxx.jpeg')
    files=['out.'+ext for ext in img_exts]
    print(files)
    print(os.getcwd())
    for file in files:
        if os.path.exists(file):
            os.remove(file)
