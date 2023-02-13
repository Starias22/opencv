import cv2 as cv
#image contours


img=cv.imread("../images/apple.jpeg")
cv.imshow("Original image",img)
#contours are used in ojects detection and reconition

"""First of all apply necessary edge detection or
treshold to the image"""
canny=cv.Canny(img,100,225)
cv.imshow("canny detection",canny)

#find contours
contours,hierarchies=cv.findContours(canny,mode=cv.RETR_TREE,method=cv.CHAIN_APPROX_SIMPLE)
print("type(contours): ",type(contours))
print("type(hierarchies): ",type(hierarchies))

print(len(contours),"contours found in the image")
#print("contours: ",contours,sep="\n")
#print("Hierarchies: ",hierarchies,sep="\n")

#draw the countours found in the image
drawnctrs=cv.drawContours(img,contours,contourIdx=-1,color=[255,0,0])
cv.imshow("Drawn contours",drawnctrs)

#Drawing the 3rd contour found in the image
thirdCtr=contours[2]
print("third contour found: ",thirdCtr)
print("type(thirdCtr): ",type(thirdCtr))
drawn3=cv.drawContours(img,[thirdCtr],0,(0,255,0),3)
cv.imshow("3rd contour drawn",drawn3)

#Drawing the last contour found in the image
lastCtr=contours[-1]
print("last contour found: ",lastCtr)
print("type(lastCtr): ",type(lastCtr))
drawnLast=cv.drawContours(img,[lastCtr],0,(0,255,0),3)
cv.imshow("last contour drawn",drawnLast)

"""#drawing contours with thresholded image
img=cv.imread("../images/cat.jpeg")
retval, threshold = cv.threshold(img, 62, 255, cv.THRESH_BINARY)
cv.imshow("tresholded cat image",threshold)
#find contours
contours,hierarchies=cv.findContours(threshold,mode= cv.CV_RETR_FLOODFILL,method=cv.CHAIN_APPROX_SIMPLE)
print(len(contours),"contours found in the cat image")
drawCtrs=cv.drawContours(img,contours,-1,[0,0,255],8)
cv.imshow("Contours drawn on the cat image",drawCtrs)"""







cv.waitKey(0)
