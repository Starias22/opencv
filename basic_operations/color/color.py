import cv2 as cv

img=cv.imread("../../images/apple.jpeg")
cv.imshow("Original",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("color gray",gray)

# bordered gray
bordered_gray=cv.copyMakeBorder(gray,20,20,20,20,cv.BORDER_CONSTANT,value=[255,0,0])
cv.imshow("bordered_gray",bordered_gray)
#remark: the border appears but not the color


cv.waitKey(0)