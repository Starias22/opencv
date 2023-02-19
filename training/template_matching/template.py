import cv2 as cv
import numpy as np
img=cv.imread('../images/cat2.jpeg')
cv.imshow("Original image",img)
#convert the image to grayscale image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grayscale cat",gray)

#read the tmeplate image
template=cv.imread("../images/cat2.jpeg")
cv.imshow('Template image',template)

#get the dimensions of the template image
dimensions=(height,width)=template.shape[:2]
print("Diemnsions: ",dimensions)

#template matching operation
tempRes=cv.matchTemplate(image=img,templ=template,method=cv.TM_CCOEFF_NORMED)

"""the template result is a grayscale image
each pixel of that image is gray if ther is no matching
and whhite otherwise"""


print("Height of the template result: ",tempRes.shape[0])
print("Width of the template result: ",tempRes.shape[1])
print("Number of pixel(s) and the template result: ",
      tempRes.shape[0]*tempRes.shape[1])

pixel=tempRes
print("pixel:",pixel)


cv.imshow('Template matching result',tempRes)
#declare a threshold:the ma should be 1
threshold=0.89
#the location
loc=np.where(tempRes>=threshold)
print("loc",loc,sep="\n")
print("type(loc):",type(loc))
print("len(loc):",len(loc))

#Draw a blue rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + width, pt[1] + height),
                 (255,0,0), 5)
# Now display the final matched template image
cv.imshow('Detected zone',img)

cv.waitKey(0)