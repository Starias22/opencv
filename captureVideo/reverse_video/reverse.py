import cv2 as cv

path='../../videos/funny.mp4'
def getFrames(path=path):
    frameList=list()
    try:
        capture=cv.VideoCapture(path)
    except cv.error:
        print('An error occured while trying to open the video!')



    #print(capture)
    #if not capture.isOpened():

    else :
        print('Video file opened successfully')
        #capture.set()
        fourcc=int(capture.get(cv.CAP_PROP_FOURCC))
        fps=int(capture.get(cv.CAP_PROP_FPS))
        width=int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
        height=int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
        frameSize=(width,height)

        while capture.isOpened():
        #read a frame
            ret,frame=capture.read()
            #if not successfully readen
            if  not ret:
                print('reading finished')
                break
            frameList.append(frame)

    capture.release()
    return frameList,fourcc,fps,frameSize


def reverse(path=path,revPath=""):
    #get the etension of the source video file
    ext=path.split('.')[-1]
    revPath='reversed.'+ext
    print(revPath)
    frames,fourcc,fps,resol=getFrames(path)
    print(len(frames),'frames readen')
    encod=''
    if ext=='mp4':
        encod='mp4v'
    #return
    try:
        fourcc=cv.VideoWriter_fourcc(*encod)
    except ValueError as v  :
        print('An  value error occured!',v)

    except TypeError  as t :
        print('An type error occured!',t)
    except  :
        print('An error**** occured!',e)
    else:
        out=cv.VideoWriter(revPath,fourcc,fps,frameSize=resol)
        for frame in frames[::-1]:
            out.write(frame)
        out.release()
        print('The video is successfully reversed')




reverse()





