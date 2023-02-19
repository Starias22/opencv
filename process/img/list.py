import cv2 as cv
import os
"""import img.writable as wrt
import img.read as reading
import img.write as wt"""

import writable as wrt
import read as reading
import write as wt
img_exts = ['bmp', 'jpg', 'jpeg', 'jpe', 'jp2', 'png',
                    'webp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']


def listImages(path=os.getcwd(),group=False):
    imgs=[]
    try:
        #if the path doesn't eist
        if not os.path.exists(path):
            raise FileNotFoundError('The provided path is not found')

        imgs=[]
        exts=[]
        for file in os.listdir(path):
            ext=file.split('.')[-1]
            if ext in img_exts:
                imgs.append(file)
                if ext not in exts:
                    exts.append(ext)
        if group:
            #print('xxx',exts)
            #print('\n\n\n\nimgs',imgs)

            grp={}
            lst=[]
            #for each extension in the extension list
            for ext in exts:
                lst.extend([elt for elt in imgs if ext==elt.split('.')[-1]])

                grp[ext]=lst
                lst=[]


    except FileNotFoundError as e:
        print(e)
        return
    if group:
        return grp
    else:
        return imgs

if __name__=='main':
    images=listImages()
    print(images)
    images=listImages('')
    images=listImages('sjfk')
    images=listImages('../../')
    print(images)
    images=listImages('../../',True)
    print(images)
    print(len(images))
    print(images.items())
    print(images.keys())
    lst=list(images.values())
    print('\n\n')
    print(lst)