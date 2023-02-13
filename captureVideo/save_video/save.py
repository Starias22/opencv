import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
fps=20.0
resolution=(640,480)
out_avi = cv.VideoWriter('output.avi',fourcc, fps, resolution)

while(cap.isOpened()):#or while True
    ret, frame = cap.read()
    if ret:
        #frame = cv.flip(frame,0)

        # write the flipped frame
        out_avi.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out_avi.release()
