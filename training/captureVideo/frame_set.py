import cv2 as cv

path='../videos/funny.mp4'
def getFrames(path=path):

    capture=cv.VideoCapture(path)
    frameList=list()

    #print(capture)
    if not capture.isOpened():
        print('An error occured while trying to open the video!')
        return []
    else :
        print('Video file opened successfully')
        #print(capture.get(cv.CAP_PROP_FRAME_COUNT))
        #return[]

        while capture.isOpened():
            #read a frame
            ret,frame=capture.read()
            #if not successfully readen
            if  not ret:
                #print(ret)
                print('Finished')
                break
            frameList.append(frame)

    capture.release()
    return frameList
frames=getFrames()
#print(frames)
print(len(frames))
rv=frames[:-1]
print(frames)
