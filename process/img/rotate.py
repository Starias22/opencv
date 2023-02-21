import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def getRotatedImg(img,center,angle,scale=1):
    """rotates an image
    Args:
        img (numpy.ndarray): the ndarray that represents the
                image to rotate
        center (tuple or list): the sequence of length 2 that
                represents the center of the rotation
        angle (float): the angle of the rotation in degree
        scale (int, optional): _the scale. Defaults to 1.

    Returns:
        numpy.ndarray: the ndarray that represents the rotated image
    """

    if img is None:
        return
    try:
        rotMatrix=cv.getRotationMatrix2D(center,angle,scale)
        dsize=(img.shape[1],img.shape[0])
        return cv.warpAffine(src=img,M=rotMatrix,dsize=dsize)

    except cv.error as e:
        print('An cv error occured',e)
    except Exception as e:
        print('An error occured',e)

def rotate(inputPath,outputPath,center,angle,scale=1):
    wt=wrt.iswritable(outputPath)
    if wt is None:
        return
    img=reading.read(inputPath)
    if img is None:
        return
    #get the exetension of the output and input files
    outext=outputPath.split('.')[-1]
    inext=inputPath.split('.')[-1]
    try:
        #assert the extension is in the exts list
        assert inext==outext
        rotMatrix=cv.getRotationMatrix2D(center,angle,scale)
        dsize=(img.shape[1],img.shape[0])
        img=getRotatedImg(img,center,angle,scale)
        if img is None or wts.imwrite(img,outputPath) is None:
            return
        return True
        #return None
    except AssertionError as e:
        print(
            'The output image extension ('+outext+')','should be as same',
                'as the input one ('+inext+')'
            )
    except cv.error as e:
        print('An cv error occured',e)
    except Exception as e:
        print('An error occured',e)


if __name__=='__main__':
    rotate('','',(0,0),45)
    rotate('','hhh',(0,0),45)
    rotate('','hhh.txt',(0,0),45)
    rotate('','hhh.png',(0,0),45)
    rotate('ks','hhh.png',(0,0),45)
    rotate('.','hhh.png',(0,0),45)
    rotate('../images/apple.jpeg','hhh.png',(0,0),45)
    rot=rotate('../images/apple.jpeg','hhh.jpeg',(0,0),45)
    import show as sh
    #sh.show2('Rotation',rot)