import cv2 as cv
img=cv.imread("../images/cat.jpeg")
cv.imshow("Cat image",img)


def simple(event,x,y,flags,param):
    print("An mouse event captured at the point",(x,y))
    if(event==cv.EVENT_LBUTTONDBLCLK):
        print('Double click event')
        #break
    """if (x,y)==(img.shape[1],img.shape[0]):
        print("Center of the image reached:")
        return"""



"""Draw circle  with radius r on click
on a point of coordinates(x,y) on the image"""
def draw_circle(event,x,y,flags,param,rad=100):
    #on the cat image, draw a circle on double click
    if(event == cv.EVENT_LBUTTONDBLCLK):

            cv.circle(img,(x,y),rad,(255,255, 0),-1)
# set callback on mouse
"""this method needs the window name and the callable, that
should be a function that handle a mouse event"""
name="draw circle on dbclick"
name="Simple tests"

cv.namedWindow(name)
cv.setMouseCallback(window_name=name,on_mouse=simple);
cv.waitKey(0)