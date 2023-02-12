import cv2 as cv
img=cv.imread("../../images/cat2.jpeg")

cv.imshow("A beautiful cat",img)

shape=img.shape
print("shape: ",shape)
print("type(shape): ",type(shape))
print("len(shape): ",len(shape))
height=shape[0]
width=shape[1]
channels=shape[2]
size=img.size
print("height: ",height)
print("width: ",width)
print("Number of channels: ",channels)
print("Image size:",size)

#The number of channels in an image is the number of color
#components inside each pixe

gray=cv.imread("../../images/cat2.jpeg",0)
shape=gray.shape
print("shape: ",shape)
print("len(shape): ",len(shape))
print("height: ",shape[0])
print("width: ",shape[1])
print("Image size:",gray.size)


#print("Number of channels in grayscal img:",gray.shape[2]) error

print("Number of dimensions  of the array representing the gray img",gray.ndim)
print("Number of dimensions  of the array representing the img: ",img.ndim)


if img.size==img.shape[0]*img.shape[1]*img.shape[2]:
    print("Alright")











cv.waitKey(0)