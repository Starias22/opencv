

import cv2 as cv
path="../videos/video.mp4"
def properties(path=path):
    #open the video
    capture=cv.VideoCapture(path)
    if not capture.isOpened():
        print('An error occured while trying to open the video.')

    else :
        print("Video opened successfuly!");
        print("***Video properties***")
        #get the resolution of the video
        #width
        width=capture.get(cv.CAP_PROP_FRAME_WIDTH)
        #height
        height=capture.get(cv.CAP_PROP_FRAME_HEIGHT)
        #get the number of frames per seconds
        fps=capture.get(cv.CAP_PROP_FPS)
        #get the total number of frames in the video
        fmscount=capture.get(cv.CAP_PROP_FRAME_COUNT)
        #get the four code character of the video
        fourcc=capture.get(cv.CAP_PROP_FOURCC)
        print(type(fourcc))
        #convert from float to int
        fourcc=int(fourcc)
        print(type(fourcc))
        fourcc = chr(fourcc & 0xFF) + chr((fourcc >> 8) & 0xFF)
        #+ chr((fourcc >> 16) & 0xFF)
        # + chr((fourcc >> 24) & 0xFF)
        print(type(fourcc))
        #print(*fourcc)
        props=dict()
        props["width"]=width
        props["height"]=height
        props["fps"]=fps
        props["fmscount"]=fmscount
        props["fourcc"]=fourcc
        return props
    capture.release()

prs=properties()
print(prs)
print("Resolution of the video:",int(prs['width']),"*",int(prs['height']))



#Let's use that function to get the duration in second of a video

def duration(path=path):
    prs=properties()
    print(prs)
    duration=prs["fmscount"]/prs["fps"]
    return int(duration)

#print(locals()['cv'])
tm=duration()
print("The video lasts",tm,'seconds')
