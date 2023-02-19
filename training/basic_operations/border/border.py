import cv2 as cv

img=cv.imread("../../images/apple.jpeg")

#src,top,bottom,left,rigth,borderType,color
replicate=cv.copyMakeBorder(img,10,15,20,25,cv.BORDER_REPLICATE)
reflect=cv.copyMakeBorder(img,10,15,20,25,cv.BORDER_REFLECT)
reflect101=cv.copyMakeBorder(img,10,15,20,25,cv.BORDER_REFLECT101)
reflect_101=cv.copyMakeBorder(img,10,15,20,25,cv.BORDER_REFLECT_101)
wrap=cv.copyMakeBorder(img,10,15,20,25,cv.BORDER_WRAP)
constant=cv.copyMakeBorder(img,10,15,20,50,cv.BORDER_CONSTANT)
constant_blue=cv.copyMakeBorder(img,10,15,20,50,cv.BORDER_CONSTANT,value=[255,0,0])


cv.imshow("original",img)
cv.imshow("replicate",replicate)
cv.imshow("reflect",reflect)
cv.imshow("reflect101",reflect101)
cv.imshow("reflect_101",reflect_101)
cv.imshow("wrap",wrap)
cv.imshow("constant",constant)
cv.imshow("constant blue",constant_blue)

cv.waitKey(0)