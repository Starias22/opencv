import cv2 as cv
import img.read as reading
import img.writable as wrt
import img.write as wt
import os
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'sr', 'ras', 'tiff', 'tif', 'pbm', 'pgm','ppm']
def gray(inputPath,outputPath):
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
        cv.imshow('Image to gray to grayscale',img)
        cv.waitKey()
        if wt.imwrite(img,outputPath):
            print('Image successfully converted to grayscale:')

    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:')

if __name__=='__main__':
    inputPath='../images/apple.jpeg'
    gray(inputPath='',outputPath='')#wrong
    gray(inputPath='skd',outputPath='wrong')#wrong
    gray(inputPath='../images/apple.jpeg',outputPath='')#wrong
    gray(inputPath,outputPath='')#wrong
    gray(inputPath,outputPath='ke')#wrong
    gray(inputPath,outputPath='out.org')#wrong
    gray(inputPath,outputPath='out.png')#right
    gray(inputPath,outputPath='out.bmp')#right
    gray(inputPath,outputPath='out.jpeg')#right
    gray(inputPath,outputPath='out.jpg')#right
    gray(inputPath,outputPath='out.jpe')#right
    gray(inputPath,outputPath='out.jp2')#right
    gray(inputPath,outputPath='out.webp')#right
    gray(inputPath,outputPath='out.ras')#right
    gray(inputPath,outputPath='out.tiff')#right
    gray(inputPath,outputPath='out.tif')#right
    gray(inputPath,outputPath='out.sr')#right
    gray(inputPath,outputPath='out.ppm')#right # doesn't support grayscale:only color images
    gray(inputPath,outputPath='out.pgm')#right doesn't support bgr
    gray(inputPath,outputPath='out.pbm')#right  doesn't support bgr
    gray('./out.sr',outputPath='out.sr')#right
    files=['out.'+ext for ext in img_exts]
    print(files)
    print(os.getcwd())
    for file in files:
        if os.path.exists(file):
            os.remove(file)
