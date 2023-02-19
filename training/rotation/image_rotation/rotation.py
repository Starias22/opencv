import cv2 as cv

#Image rotation
img=cv.imread("../../images/cat.jpeg")
cv.imshow("Original image( of cat): ",img)

#2Drotation matrix


#the center of the rotation
center=(0,0)
#the angle of the rotation
angle=45
#the scale of the rotation
scale=1
rMatrix2D=cv.getRotationMatrix2D(center,angle,scale)
dimensions=(img.shape[1],img.shape[0])
rotated45=cv.warpAffine(img,rMatrix2D,dimensions)
cv.imshow("rotated 45 from (0,0)",rotated45)

#the center of the image,90 degree
center=(img.shape[1]/2,img.shape[0]/2)
angle=90
rMatrix2D=cv.getRotationMatrix2D(center,angle,scale)
rotated90=cv.warpAffine(img,rMatrix2D,dimensions)
cv.imshow("rotated 90 from the center",rotated90)

#the center of the image,90 degree
angle=125
rMatrix2D=cv.getRotationMatrix2D(center,angle,scale)
rotated125=cv.warpAffine(img,rMatrix2D,dimensions)
cv.imshow("rotated 125 from the center",rotated125)

#the center of the image,180 degree
angle=180
rMatrix2D=cv.getRotationMatrix2D(center,angle,scale)
rotated180=cv.warpAffine(img,rMatrix2D,dimensions)
cv.imshow("rotated 180 from the center",rotated180)

#the center of the image,360 degree
angle=360
rMatrix2D=cv.getRotationMatrix2D(center,angle,scale)
rotated360=cv.warpAffine(img,rMatrix2D,dimensions)
cv.imshow("rotated 360 from the center",rotated360)

cv.waitKey(0)


