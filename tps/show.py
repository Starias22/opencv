import cv2 as cv
import read as rd

def show2(label,img):
    if img is None:
        return
    cv.waitKey(0)
    name=label
    cv.imshow(name,img)
    print('Press Q/q to exit')
    while True:
        #wait undefinitely for a key to continue
        key=cv.waitKey()
        #if Q/q pressed
        if key==ord('q'):
        #cv.destroyAllWindows()
            #exit
            break


def show(inputPath):
    img=rd.read(inputPath)
    if img is None:
        return
    cv.waitKey(0)
    name=inputPath.split('/')[-1]
    cv.imshow(name,img)
    print('Press Q/q to exit')
    while True:
        #wait undefinitely for a key to continue
        key=cv.waitKey()
        #if Q/q pressed
        if key==ord('q'):
        #cv.destroyAllWindows()
            #exit
            break
if __name__=='__main__':
    show('')
    show(('../images/apple.jpeg'))
    #show('label',)