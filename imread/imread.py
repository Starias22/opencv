import cv2 as cv
#the name of the image
name="../images/cat.jpeg"
img=cv.imread(name)
label="My cat"
#Show the image with label
cv.imshow(label,img)

print('type(img)',type(img))
print("img:",img)

cv.waitKey(0)

