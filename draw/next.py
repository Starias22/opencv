import numpy as np
import cv2 as cv
img = cv.imread("../images/cat.jpeg",cv.IMREAD_COLOR)
#defining points for polylines
pts = np.array([[96,72],[200,115],[115,20],[10,10]], np.int32)
# pts = pts.reshape((-1,1,2))
cv.polylines(img, [pts], True, (0,255,255), 3)
cv.imshow('image',img)

font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img,'Hack Projects',(10,500), font, 1,(255,255,255),2)
#Display the image
cv.imshow("Text added",img)

cv.waitKey(0)
