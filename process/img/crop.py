import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt



def getCropedImg(img,x1,y1,x2,y2):
    """Crop an image and return the rectangle matchin the region
    of interest(ROI).

    Args:
        img (numpy.ndarray): the ndarray that represents the image to crop
        x1 (int): the top of the ROI
        y1 (int): the left of the ROI
        x2 (int): the bottom of the ROI
        y2 (int):the riht of the ROI

    Raises:
        TypeError: when x1,x2,y1 or y2 is not positive integer or when
        x1 is greather than x2 or when y1 is rather than y2
        ValueError: if the width or height of the new image is null

    Returns:
        numpy.ndarray: the ndarray that represents the new image
    """
    try:
        if (type(x2)!=type(0) or type(y2)!=type(0))or (type(x1)!=type(0)
        or type(y1)!=type(0)):
            raise TypeError('Width and height should be integers')
        if (x1<=0 or x2<=0) or(y1 or y2):
            raise TypeError('Width and height should be positive and not null')

        if x1>x2:
            raise TypeError('The bottom agument should be greater than the top one')

        if y1>y2:
            raise TypeError('The rigth agument should be greater than the left one')
        #if failure
        if img is None:
            #nothing else to do
            return
        #height,width=(img.shape[0],img.shape[1])
        #else
        print('Old width:',img.shape[1])
        print('Old height:',img.shape[0])
        img=img[y1:y1+y2,x1:x1+x2]
        print('New width:',img.shape[1])
        print('New height:',img.shape[0])
        if  img.shape[1]==0:
            raise ValueError("The new image's width is null")
        elif img.shape[0]==0:
            raise ValueError("The new image's height is null")
        return img
    except TypeError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except IndexError as e:
        print('You exced the image zone',e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print('An unknown error occured:',e)

def crop(inputPath,outputPath,x1,y1,x2,y2):
    """crops an image

    Args:
        inputPath (str): the input path of the image to crop
        outputPath (str): the output path of the cropped image
        x1 (int): the top of the ROI
        y1 (int): the left of the ROI
        x2 (int): the bottom of the ROI
        y2 (int):the riht of the ROI
    Returns:
        bool: True if the cropping is successfull
    """
    #img reading
    try:
        wrtable=wrt.iswritable(outputPath)
        if  wrtable is None:
            return
        #try to read the image
        img=reading.read(inputPath)
        #if failure
        if img is None:
            #nothing else to do
            return
        #else
        #get the exetension of the output and input files
        outext=outputPath.split('.')[-1]
        inext=inputPath.split('.')[-1]
        #assert the extension is in the exts list
        assert inext==outext

        img=getCropedImg(img,x1,y1,x2,y2)
        if img is None:
            return
        if wt.imwrite(img,outputPath):
            print('Image successfully croped to',outputPath)
            return True
        return
    except AssertionError as e:
        print(
            'The output image extension ('+outext+')','should be as same',
                'as the input one ('+inext+')'
            )
    except TypeError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:',e)

if __name__=='__main__':
    help(getCropedImg)
    inputPath='../src/images/apple.jpeg'
    crop('','',20,20,20,20)#wrong
    crop('skd','wrong',20,20,20,20)#wrong
    crop('../src/images/apple.jpeg','',20,20,20,20)#wrong
    crop('../src/images/apple.jpeg','out.png','kk',20,20,20)#wrong
    crop('../src/images/apple.jpeg','out.png',20,'jkd',20,20)#wrong
    crop('../src/images/apple.jpeg','out.png',20,True,20,20)#wrong
    crop('../src/images/apple.jpeg','out.jpeg',56.5,1,20,20)#wrong
    """crop('../src/images/apple.jpeg','out.png',-20,20,20,20)#wrong
    crop('../src/images/apple.jpeg','out.png',20,20,20,20)#wrong
    crop('../src/images/apple.jpeg','out.jpeg',0,0,20,20)#wrong
    crop('../src/images/apple.jpeg','out.jpeg',0,200,20,20)#wrong"""
    crop('../src/images/apple.jpeg','out.jpeg',0,0,100,300)#good







