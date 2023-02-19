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
print(cv.error)

#img=cv.imread("doesntexist")
#print(img)#none
#cv.imshow(label,img)

#a svg e, not supported by opencv
#git_svg=cv.imread("../images/github.svg")
#print(git_svg)
#cv.imshow(label,git_svg)

def read(path,label='image'):
    try:
        img=cv.imread(path)
        cv.imshow(label,img)
        cv.waitKey(0)
    except cv.error:
        print("The image cannot be readen")

read('../images/apple.jpeg','apple')
read('error')

