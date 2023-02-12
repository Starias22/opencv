import cv2 as cv
img=cv.imread("../../images/cat2.jpeg")

#cv.imshow("A beautiful cat",img)
b,g,r=cv.split(img)

print("blue:",b)
print("type(blue):",type(b))

#merging:a tuple as arg
merged=cv.merge((b,g,r))

cv.imshow("Original image",img)
cv.imshow("Merged image",merged)
#we can save the merged image

if cv.imwrite("merged.jpeg",merged):
    print("Merged image saved")

#compare the merged image wih the original one

if img.shape==merged.shape:
    print("Same height, width and number of channels")
if img.size==merged.size:
    print("Same number of pixels")


blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]

print("blue:",blue)
print("type(blue):",type(blue))

"""if b==blue:
    print("they are equal")"""

#merging

mrg=cv.merge((blue,green,red))
cv.imshow("Merged image2",mrg)


if img.shape==mrg.shape:
    print("Same height, width and number of channels")
if img.size==mrg.size:
    print("Same number of pixels")


#the slicing method is the recommended one because more faster




cv.waitKey(0)




