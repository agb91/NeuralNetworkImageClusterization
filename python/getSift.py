import cv2
import numpy as np
from matplotlib import pyplot as plt

def readGrayImage( path ):
	img = cv2.imread( path )
	gray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
	return gray

def getSiftKeypoint( greyImage ):
	detector = cv2.SIFT()
	#kp = detector.detect( greyImage , None )
	kp, des = detector.detectAndCompute( greyImage , None )
	return des

def writeImageOnFile( path , gray , kp ):
	img = cv2.drawKeypoints( gray , kp )
	cv2.imwrite( path , img )
	

gray1 = readGrayImage( '/home/andrea/Desktop/neuroph/images/elephantShape.png' )
gray2 = readGrayImage ( '/home/andrea/Desktop/neuroph/images/elephantShape.png' )

des1 = getSiftKeypoint( gray1 )
des2 = getSiftKeypoint( gray2 )

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

print len(good)

#writeImageOnFile( '/home/andrea/Desktop/neuroph/images/output1.jpg' , gray1 , kp1 )
#writeImageOnFile( '/home/andrea/Desktop/neuroph/images/output2.jpg' , gray2 , kp2 )
#print kp[0]
