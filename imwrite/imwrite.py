import cv2 as cv
#color image
img_src=cv.imread("../images/cat2.jpeg")

#im writing


if cv.imwrite("newimg.jpg",img_src)==True:
    print("Image saved")

#grayscale image
img_src=cv.imread("../images/cat2.jpeg",cv.IMREAD_GRAYSCALE)

cv.imwrite("grayscle.jpeg",img_src)
#overwritten in case of existence
cv.imwrite("grayscle.jpeg",img_src)


cv.waitKey(0)