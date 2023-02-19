import cv2 as cv

capture=cv.VideoCapture('../videos/video.mp4')
fps = capture.get(cv.CAP_PROP_FPS)
print(fps,"frames per second in that video")
count=0

"""display the frame while the user press a
key different from q
if he presses q exit and
output the number of frames captured"""
while True:
    ret,frame=capture.read()
    print()
    count+=1
    print("An image captured: ",count)
    #we can same the frame if we want
    #we can put test on image, etc
    cv.imshow("My video",frame)
    key=cv.waitKey(0)
    if key==ord('q'):# q or Q
        print("You have exited")
        break
capture.release() #free the camera
print(count,"frame(s) captured at all")




capture=cv.VideoCapture('../videos/video.mp4')

count=0

"""display the frame while the user press a
key different from q
if he presses q exit and
output the number of frames captured"""
while True:
    ret,frame=capture.read()
    print()
    count+=1
    print("An image captured: ",count)
    #we can same the frame if we want
    #we can put test on image, etc
    cv.imshow("My video: frame",frame)
    if count==2:
        cv.imwrite("./dest/video_frame.png",frame)
        print("Second frame saved as png file")
    key=cv.waitKey(1)
    if key==ord('q'):# q or Q
        print("You have exited")
        break
capture.release() #free the camera
print(count,"frame(s) captured at all")

