import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
def getProperties(inputPath):

    img=reading.read(inputPath)
    if img is None:
        return
    height=0
    width=0,
    nbchannels=0
    size=0
    gray=False
    props={}
    name=inputPath.split('/')[-1]
    try:
        height,width,nbchannels=img.shape
        size=img.size

    except IndexError :
        nbchannels=1
        gray=True
    finally:

        props['name']=name
        props['height']=height
        props['width']=width
        props['gray']=gray
        props['nbchs']=nbchannels
        props['size']=size
        return props

if __name__=='__main__':
    inputPath='../images/apple.jpeg'
    getProperties(inputPath='')#wrong
    getProperties(inputPath='skd')#wrong
    val=getProperties(inputPath='../images/apple.jpeg')
    print(val)
    print(getProperties('./out.jpeg'))

