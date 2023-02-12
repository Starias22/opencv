import numpy as np
import cv2 as cv
img = cv.imread("../images/cat.jpeg",cv.IMREAD_COLOR)
cv.imshow('original image',img)
canny=cv.Canny(img,100,200)
cv.imshow('Edge detection with canny',canny)

cv.waitKey(0)