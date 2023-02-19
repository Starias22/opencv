import cv2 as cv

img=cv.imread("../images/apple.jpeg")
cv.imshow("image",img)
tims=5000
cv.waitKey(tims)
"""wait  a key press for 5000ms
ie 5s and passes to the next lines.
If a key is pressed befor 5s the programm will stop
waiting and the next lines will be executed"""
print("time passed or key pressed:",tims,"ms")

cv.imshow("image",img)
cv.waitKey(0) #wait indefinitly until a key is pressed
print("Key pressed")


cv.imshow("image",img)
key=cv.waitKey() #wait indefinitly until a key is pressed
#return the ASCII code of the pressed key in a owercase representation
print("Key pressed:",key)
if key==ord('A'):#will be necessary false
    print('A is pressed')
else :
    print('A isn\'t pressed')

print("ord('A')=",ord('A'))


print("Waiting 5s  for key event")
key=cv.waitKey(5000)
if key==-1:
    print("No key is pressed")


