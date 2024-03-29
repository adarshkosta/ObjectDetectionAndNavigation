import numpy as np
import cv2
import glob
 
# initialize the camera and grab a reference to the raw camera capture


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


# grab an image from the camera
#camera.capture(rawCapture, format="bgr")
#img = rawCapture.array
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.imwrite('chessCalib.jpg', gray)
cv2.waitKey(0)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (6, 6),None)
print corners
# If found, add object points, image points (after refining them)
if ret == True:
	objpoints.append(objp)

	corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
	imgpoints.append(corners2)

	# Draw and display the corners
	img = cv2.drawChessboardCorners(img, (6,6), corners2,ret)
	#cv2.imwrite('output',img)
	#cv2.waitKey(0)
#else:
	#print corners
cv2.destroyAllWindows()