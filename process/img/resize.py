import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def getResizedImg(img,height,width):
    """resize an image
    Args:
        img (numpy.ndarray): the ndarray that represents the image
        height (int): the new height to apply to the image
        width (int): the new width to apply to the image
    Raises:
        TypeError: if the height or the width is not float, or is negative
    Returns:
        None:if failure
    """
    #img reading
    try:
        if type(height)!=type(0) or type(width)!=type(0):
            raise TypeError('Width and height should be integers')
        if height<=0 or width<=0:
            raise TypeError('Width and height should be positive and not null')
        #if failure
        if img is None:
            #nothing else to do
            return
        #else

        dimens=(width,height)
        img=cv.resize(img,dimens)
        return img
    except TypeError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:',e)


def resize(inputPath,outputPath,height,width):
    """resize an image
    Args:
        inputPath (str): the  path of  the image file
        height (int): the new height to apply to the image
        width (int): the new width to apply to the image
    Raises:
        TypeError: if the height or the width is not float, or is negative


    Returns:
        None: if failure
        bool: True otherwise
    """

    #img reading
    try:
        wrtable=wrt.iswritable(outputPath)
        if  wrtable is None:
            return

        if type(height)!=type(0) or type(width)!=type(0):
            raise TypeError('Width and height should be integers')

        if height<=0 or width<=0:
            raise TypeError('Width and height should be positive and not null')
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

        img=getResizedImg(img,height,width)
        if wt.imwrite(img,outputPath):
            print('Image successfully resized to',outputPath)
            return True
        return None
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
    inputPath='../images/apple.jpeg'
    resize('','',20,20)#wrong
    resize('skd','wrong',20,20)#wrong
    resize('../images/apple.jpeg','',20,20)#wrong
    resize('../images/apple.jpeg','out.png','kk',20)#wrong
    resize('../images/apple.jpeg','out.png',20,'jkd')#wrong
    resize('../images/apple.jpeg','out.png',20,True)#wrong
    resize('../images/apple.jpeg','out.jpeg',56.5,1)#wrong
    resize('../images/apple.jpeg','out.png',-20,20)#wrong
    resize('../images/apple.jpeg','out.png',20,20)#wrong
    resize('../images/apple.jpeg','out.jpeg',0,0)#wrong
    resize('../images/apple.jpeg','out.jpeg',0,200)#wrong
    resize('../images/apple.jpeg','out.jpeg',200,45)#good







