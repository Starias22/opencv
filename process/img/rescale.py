
import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt


def getRescaledImg(img,hscale,wscale):
    """rescale an image
    Args:
        img (numpy.ndarray): the ndarray that represents the image
        hscale (float): the scale to apply to the image height
        wscale (float): the scale to apply to the image width
    Raises:
        TypeError: if the hscale of the wscale is not integer
            or float, or is negative.


    Returns:
        None: if failure
        numpy.ndarray: the ndarray that represents the
            rescaled image if success
    """
    #img reading
    try:
        if not isinstance(hscale, (int, float)) or not isinstance(wscale, (int, float)):
            raise TypeError('Width and height should be floats or integers')

        if hscale<=0 or wscale<=0:
            raise TypeError('Width scale and height scale should be positive and not null')
        #if failure
        if img is None:
            #nothing else to do
            return
        #else
        width=int(img.shape[1]*wscale)
        height=int(img.shape[0]*hscale)
        dimens=(width,height)
        img=cv.resize(img,dimens)
        return img
    except TypeError as e:
        print(e)
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An unknown error occured:',e)




def rescale(inputPath,outputPath,hscale,wscale):
    """rescale an image
    Args:
        img (numpy.ndarray): the ndarray that represents the image
        outputPath(str):the destination of the rescaled image
        hscale (float): the scale to apply to the image height
        wscale (float): the scale to apply to the image width
    Raises:
        TypeError: if the hscale or the wscale is not integer or
            float, or is negative
    Returns:
        None: if failure
        True: if success
    """
    #img reading
    try:
        wrtable=wrt.iswritable(outputPath)
        if  wrtable is None:
            return
        if not isinstance(hscale, (int, float)) or not isinstance(wscale, (int, float)):
            raise TypeError('Width and height should be floats or integers')

        if hscale<=0 or wscale<=0:
            raise TypeError('Width scale and height scale should be positive and not null')
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
        width=int(img.shape[1]*wscale)
        height=int(img.shape[0]*hscale)
        dimens=(width,height)
        img=getRescaledImg(img,hscale,wscale)
        #write to the output file
        if wt.imwrite(img,outputPath):
            print('Image successfully rescaled to',outputPath)
            return True
        else:
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
    rescale('','',20,20)#wrong
    rescale('skd','wrong',20,20)#wrong
    rescale('../images/apple.jpeg','',20,20)#wrong
    rescale('../images/apple.jpeg','out.png','kk',20)#wrong
    rescale('../images/apple.jpeg','out.png',20,'jkd')#wrong
    rescale('../images/apple.jpeg','out.png',20,True)#wrong
    rescale('../images/apple.jpeg','out.jpeg',56.5,1)#good
    rescale('../images/apple.jpeg','out.png',-20,20)#wrong
    rescale('../images/apple.jpeg','out.png',20,20)#wrong
    rescale('../images/apple.jpeg','out.jpeg',0,0)#wrong
    rescale('../images/apple.jpeg','out.jpeg',0,200)#wrong
    rescale('../images/apple.jpeg','out.jpeg',0.55,1.5)#good







