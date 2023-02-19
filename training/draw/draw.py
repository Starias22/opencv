import cv2 as cv

img=cv.imread("../images/cat2.jpeg")
cv.imshow("Original image",img)
#drawing shapes
#circle
center=(50,45)
radius=50
color=[255,0,0]#blue(BGR)
circle=cv.circle(img,center,radius,color)
cv.imshow("Blue circle drawn on image",circle)


cv.imshow("Original",img)
#remark

circle=cv.circle(img,center,radius,[0,255,0],thickness=-1)
cv.imshow("Filled green circle drawn on image",circle)

#rectangle

point1=(150,80)
point2=(75,104)
color=[0,0,255]#red
rect=cv.rectangle(img,point1,point2,color,thickness=-15)#the 2 last args is opt
cv.imshow("Filled red rectangle drawn on image",rect)
#line
point1=(45,80)
point2=(75,180)
color=[88,15,255]
line=cv.line(img,point1,point2,color,5)
cv.imshow("Filled red rectangle drawn on image",line)
cv.waitKey(0)

