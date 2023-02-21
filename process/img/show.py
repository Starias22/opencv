import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def show2(label,img):
    """shows an image
    Args:
        label (str): the name of the window
        img (numpy.ndarray): the ndarray that represents the image to show
    """
    if img is None:
        return
    cv.waitKey(0)
    name=label
    cv.imshow(name,img)
    print('Press Q/q to exit')
    while True:
        #wait undefinitely for a key to continue
        key=cv.waitKey()
        #if Q/q pressed
        if key==ord('q'):
        #cv.destroyAllWindows()
            #exit
            break

def show(inputPath):
    """shows an image
    Args:
        inputPath (str): the path of the input image file to show
    """
    img=reading.read(inputPath)
    if img is None:
        return
    cv.waitKey(0)
    name=inputPath.split('/')[-1]
    cv.imshow(name,img)
    print('Press Q/q to exit')
    while True:
        #wait undefinitely for a key to continue
        key=cv.waitKey()
        #if Q/q pressed
        if key==ord('q'):
        #cv.destroyAllWindows()
            #exit
            break
if __name__=='__main__':
    show('')
    show('./out.jpeg')
    #show(('../src/images/apple.jpeg'))
    #show('label',)