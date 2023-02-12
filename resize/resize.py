import cv2 as cv
img=cv.imread("../images/apple.jpeg")

cv.imshow("Original apple",img)
print("Hight:",img.shape[0],"Width:",img.shape[1])
#Image resizing
#option1: maintain the aspet ratio: image rescaling
    #a:downscale:decrease the dimensions of the image
#The image dimensions ie width and height will be devided by 2 ie multiplied by 0.5
dheight=img.shape[0]//2
dwidth=int(img.shape[1]*0.5)
dimensions=(dwidth,dheight)
dresized=cv.resize(img,dimensions)
cv.imshow("Downscaled image",dresized)
print("Height of the downscaled image",dresized.shape[0])
print("Width of the downscaled image",dresized.shape[1])

if dheight==dresized.shape[0] and dwidth==dresized.shape[1]:
    print("Alright")



    #a:upscale:increase the dimensions of the image
    #The image dimensions ie width and height will be multiplied by 1.5
iheight=int(img.shape[0]*1.5)
iwidth=int(img.shape[1]*1.5)
dimensions=(iwidth,iheight)
iresized=cv.resize(img,dimensions)
cv.imshow("Upscaled image",iresized)
print("Height of the upscaled image",iresized.shape[0])
print("Width of the upscaled image",iresized.shape[1])

if iheight==iresized.shape[0] and iwidth==iresized.shape[1]:
    print("Alright")


#option2:don't maintain the aspet ratio
    #a:upscale:increase the dimensions of the image

#change the height only
dimensions=(img.shape[1],125)
resized=cv.resize(img,dimensions)
cv.imshow("Resized image(the height only)",iresized)
print("Height of the resized image",resized.shape[0])
print("Width of the resized image",resized.shape[1])

#change the width only
dimensions=(int(img.shape[1]*0.65),img.shape[0]) #height unchanged
resized=cv.resize(img,dimensions)
cv.imshow("Resized image(the width only)",iresized)
print("Height of the resized image",resized.shape[0])
print("Width of the resized image",resized.shape[1])

#change both the width and the height
dimensions=(int(img.shape[1]*0.65),90)
resized=cv.resize(img,dimensions)
cv.imshow("Resized image(both)",iresized)
print("Height of the resized image",resized.shape[0])
print("Width of the resized image",resized.shape[1])
cv.waitKey(0)