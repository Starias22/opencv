import numpy as np
import cv2 as cv
img = cv.imread("../images/cat.jpeg",cv.IMREAD_COLOR)
cv.imshow('original image',img)
#average blur
blured=cv.blur(img,(3,3))
cv.imshow('(average) blured image',img)

#Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Gaussian-blured image',gauss)

#median blur
blured=cv.medianBlur(img,3)
cv.imshow('median blured image',img)

cv.waitKey(0)