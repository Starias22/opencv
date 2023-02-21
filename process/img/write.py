import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def imwrite(img,outputPath):
    """writes an image to the specified output path

    Args:
        img (numpy.ndarray): the ndarray that represents the image
        to write to an output path
        outputPath (str): the output file path to write image to

    Returns:
        bool:True if the writing is successfull
        None:if failure
    """
    wt=wrt.iswritable(outputPath)
    if wt is None:
        return
    if img is None:
        return
    try:
        cv.imwrite(outputPath,img)
    except cv.error as e:
        print('An cv error occured:',e)
    except Exception as e:
        print('An occured:',e)
    else:
        return True

if __name__=='__main__':
    pass
    #imwrite('','out.png')