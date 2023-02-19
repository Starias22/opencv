import cv2 as cv

#img=cv.imread("../images/cat2.jpeg",cv.IMREAD_GRAYSCALE)
#img=cv.imread("../images/cat2.jpeg",cv.IMREAD_COLOR)
img=cv.imread("../images/cat2.jpeg",cv.IMREAD_UNCHANGED)
cv.imshow("A cat",img)
cv.waitKey(0)