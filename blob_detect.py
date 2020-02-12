#!/usr/bin/python

# Standard imports
import cv2
import numpy as np

# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture(0)
i = 0

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.2

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

while(True):
# Detect blobs.
	#keypoints = detector.detect(im)
	ret, frame = cap.read()
	keypoints = detector.detect(frame)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

	#im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cap_w_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	img = np.zeros((500,500,3),dtype = 'uint8') # Create a dummy image
	
# Show blobs
	#cv2.imshow("Keypoints", im_with_keypoints)
	cv2.imshow('frame',cap_w_keypoints)
	#cv2.waitKey(0)
	cv2.imshow('a',img)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,chr(1),(140+i,250), font, .5,(255,255,255),2,cv2.LINE_AA)
	i+=10
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()
