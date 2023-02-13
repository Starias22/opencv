import cv2 as cv
import numpy as np
#read the image
img=cv.imread("../images/apple.jpeg")
cv.imshow("Original image",img)

#image filters: bilateralFilter, boxFilter and filter2D
#bilateral filter
blur=cv.bilateralFilter(img,7,15,16)
cv.imshow("Bilateral filter1",blur)

blur2=cv.bilateralFilter(img,7,100,150)
cv.imshow("Bilateral filter2",blur2)

#box filter
box_filter=cv.boxFilter(img,0, (7,7), img, (-1,-1), False, cv.BORDER_DEFAULT)
cv.imshow("Box filter",box_filter)

#filter2D
kernel = np.ones((5,5),np.float32)/25#5*5 matrix of 0.4 as value
print("kernel: ",kernel,sep="\n")
filter2D = cv.filter2D(img,-1,kernel)
cv.imshow("Filter2D",filter2D)


cv.waitKey(0)