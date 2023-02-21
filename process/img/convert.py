import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt

#list of the supported extensions
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']

def convert(inputPath,outputPath):
    """converts an image from a format to another.

    Args:
        inputPath (str): the path of the input file
        outputPath (str): the path of the output file
    """

    try:
        #check if the output path can be written to
        wtb=wrt.iswritable(outputPath)
        #otherwise
        if wtb is None:
            return
        #the output file is writable
        #try to read the image
        img=reading.read(inputPath )
        #if failure
        if img is None:
            #nothing else to do
            return
        #else
        #get the exetension of the output file
        ext=outputPath.split('.')[-1]
        #if the extension is ppm
        if ext=='ppm':
            #if img is not bgr
            if len(img.shape)!=3:
                print("Conversion impossible: You're using",ext,"file extension which doesn't support",
                        'grayscale while the input file is grayscale.\n')
                return

        #if the extension is pgm or pbm
        if ext =='pgm' or ext=='pbm':
            if len(img.shape)==3:
                print("You're using",ext,"file extension which doesnt support",
                        'bgr while the input file is bgr.\n','Press O/o if you',
                        'want the output file be a grayscale image.\n',
                        'Press any key else to exit')
                cv.imshow('Image to convert',img)
                key=cv.waitKey(0)
                #if O/o not pressed
                if key!=ord('o'):
                    #print('****key:',key)
                    print('Converting aborted!')
                    return
                #else(O/ key is pressed)
                #convert img to grayscale
                img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        """print('File converting: Press a key to continue')
        #show the image
        cv.imshow('Image to convert',img)
        #wait for a key to continue
        cv.waitKey()"""
        if wt.imwrite(img,outputPath):
            print('Image successfully converted to',ext)
            return True
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:')

if __name__=='__main__':
    help(convert)
    inputPath='../images/apple.jpeg'

    convert(inputPath='',outputPath='')#wrong
    convert(inputPath='skd',outputPath='wrong')#wrong
    convert(inputPath='../images/apple.jpeg',outputPath='')#wrong
    convert(inputPath,outputPath='')#wrong
    convert(inputPath,outputPath='ke')#wrong
    convert(inputPath,outputPath='out.org')#wrong

    convert(inputPath,outputPath='out.png')#right
    convert(inputPath,outputPath='out.bmp')#right
    convert(inputPath,outputPath='out.jpeg')#right
    convert(inputPath,outputPath='out.jpg')#right
    convert(inputPath,outputPath='out.jpe')#right
    convert(inputPath,outputPath='out.jp2')#right
    convert(inputPath,outputPath='out.webp')#right
    convert(inputPath,outputPath='out.ras')#right
    convert(inputPath,outputPath='out.tiff')#right
    convert(inputPath,outputPath='out.tif')#right
    convert(inputPath,outputPath='out.sr')#right
    convert(inputPath,outputPath='out.ppm')#right # doesn't support grayscale:only color images
    convert(inputPath,outputPath='out.pgm')#right doesn't support bgr
    convert(inputPath,outputPath='out.pbm')#right  doesn't support bgr

    convert('./out.sr',outputPath='out.sr')#right

    files=['out.'+ext for ext in img_exts]
    print(files)
    print(os.getcwd())

    for file in files:
        if os.path.exists(file):
            os.remove(file)
