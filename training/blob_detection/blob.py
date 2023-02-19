import cv2 as cv
import numpy as np;

img = cv.imread("../images/cat2.jpeg", cv.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector()

print("detection:",detector)
print("type(detector):",type(detector))

# Detecting blobs.
keypoints = detector.detect(img)
"""
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                        cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Show keypoints
cv.imshow("Keypoints", im_with_keypoints)
cv.waitKey(0)"""