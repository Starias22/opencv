import cv2 as cv
import numpy as np
img=cv.imread("../images/cat.jpeg")
cv.imshow('Original image',img)
shape=(5,5)
matrix=np.ones(shape)
print("matrix.shape",matrix.shape)

dilated=cv.dilate(img,matrix)
cv.imshow('Dilated image',dilated)

eroded=cv.erode(img,matrix,iterations=1)
cv.imshow('Eroded image',eroded)

cv.waitKey(0)
