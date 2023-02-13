import cv2 as cv
img=cv.imread("../../images/cat.jpeg")

#Pixel is the smallest unit of data in an image

#get the pixel value of img at the pos (100,100)
pixel=img[100,100]
print("pixel:",pixel)
print("type(pixel):",type(pixel))
#It represents the quantity of blue, green and
# red at the specified position

print("Blue:",pixel[0])
print("Green:",pixel[1])
print("Red:",pixel[2])
red=pixel[2]
print("red=pixel[2];;;type(red):",type(red))

#grayscale image
img=cv.imread("../../images/cat.jpeg",0)

#get the pixel value of gray scale img at the pos (100,100)
pixel=img[100,100]
print("pixel:",pixel)
print("type(pixel):",type(pixel))
#It represents the quantity of dark and light
# at the specified position of the image
#It's an it that ranges from 0 to 255
# 0: the darkest shade of gray
# 255: the lightest shade of gray


#the image size is the total number of elements ie pixels in the image

print("Total number of pixels",img.size)