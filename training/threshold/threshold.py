import cv2 as cv
img=cv.imread("../images/cat.jpeg")
cv.imshow("Original cat",img)
#image tresholding
#goal:simplify image data visualisation and analysis

retval, threshold = cv.threshold(img, 62, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded image:",threshold)


img=cv.imread("../images/cat2.jpeg")
cv.imshow("Original cat1",img)

retval, threshold = cv.threshold(img, 62, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded cat2:",threshold)

img=cv.imread("../images/apple.jpeg")
cv.imshow("Original apple",img)
retval, threshold = cv.threshold(img, 62, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded apple:",threshold)

img=cv.imread("../images/text.png")
cv.imshow("Original tet",img)
retval, threshold = cv.threshold(img, 62, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded text:",threshold)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscal text",gray)
retval, threshold = cv.threshold(gray, 62, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded grayscale text:",threshold)

cv.waitKey(0)