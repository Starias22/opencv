import cv2 as cv
from math import radians, cos,sin,pi


#2D rotation matrix
"""A 2D rotation matrix is the matrix used to rotate
points in 2D around a point, with a specific angle"""
#the center of the rotation
center=(0,0)
#the angle of the rotation
angle=45
#the scale of the rotation
scale=1
rMatrix=cv.getRotationMatrix2D(center,angle,scale)
print("rotation Matrix: ",rMatrix,sep="\n")
print("type(rMatrix): ",type(rMatrix))


print("cos(pi/4)=",cos(pi/4))
print("sin(pi/4)=",sin(pi/4))

angle_rad=radians(angle)
print("cos(",angle,")=",cos(angle_rad))
print("sin(",angle,")=",sin(angle_rad))


