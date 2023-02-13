import cv2 as cv

#take a real time picture

capture=cv.VideoCapture(0)
print("capture:",capture)
print("type(capture): ",type(capture))
ret,frame=capture.read()
print("ret=",ret)
if ret:
    #some properties of the captured fram
    print("Frame successfully captured")
    cv.imshow("Captured frame",frame)
    print("Height:",frame.shape[0],"Width:",frame.shape[1])
    print(frame.shape[2],"channels")
    print("Size=number of pixels:",frame.size)
    #save the frame in different formats
    cv.imwrite("dest/frame.jpeg",frame)
    cv.imwrite("dest/frame.jpg",frame)
    cv.imwrite("dest/frame.png",frame)
    cv.imwrite("dest/frame.bmp",frame)
    cv.imwrite("dest/frame.ppm",frame)
    cv.imwrite("dest/frame.tiff",frame)
    cv.imwrite("dest/frame.tif",frame)
    cv.imwrite("dest/frame.webp",frame)
    #cv.imwrite("dest/frame.pbm",frame)
    #cv.imwrite("dest/frame.exr",frame)
    #cv.imwrite("dest/frame",frame)
    #cv.imwrite("dest/frame.svg",frame)
    #grayscale
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imwrite("gray/frame.png",gray)


else:
    print("An error occured!")
capture.release()
cv.waitKey(0)

#real time video
capture=cv.VideoCapture(0)
print("capture:",capture)
print("type(capture): ",type(capture))
count=0
while True:
    ret,frame=capture.read()
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
print("capture:",capture)
print("type(capture): ",type(capture))
print(count,"image(s) captured at all")

#display all the frames

capture=cv.VideoCapture(0)
count=0
while True:

    ret,frame=capture.read()
    #do wathever you wan't with the frame
    count+=1
    cv.imshow("frame"+str(count),frame)
    key=cv.waitKey(1000)
    if key!=-1:
        print("Exited")
        break
    #cv.destroyAllWindows()

#be default all the frame will be displayed


capture.release()#free the camera

