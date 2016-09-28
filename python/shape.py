# import the necessary packages
import cv2
import sys
import os
from os import walk
import math

def getArrayGrid( max , space ):
	ris = []
	howMany = int( math.floor( max / space ) )
	for x in range( howMany ):
		toAdd = x * space
		ris.append( toAdd )
	return ris

def checkAxis(  )

def getShape( image ):
	height, width = image.shape[:2]
	arrayWidth = getArrayGrid( width , 10 )
	arrayHeight = getArrayGrid( height , 10 )
	arrayMaxX = []
	arrayMinX = []
	arrayMaxY = []
	arrayMinY = []
	for x in arrayWidth:
		thisMax = 0
		thisMin = height - 1
		for y in range( height ):
			if image[ y , x ] < 30:
				if y < thisMin:
					thisMin = y
				if y > thisMax:
					thisMax = y
		arrayMinX.append( thisMin )
		arrayMaxX.append( thisMax )	
	for y in arrayHeight:
		thisMax = 0
		thisMin = width - 1
		for x in range( width ):
			if image[ y , x ] < 30:
				if x < thisMin:
					thisMin = x
				if x > thisMax:
					thisMax = x
		arrayMinY.append( thisMin )
		arrayMaxY.append( thisMax )	
	print arrayMaxY
	print arrayMinY
	print arrayMaxX
	print arrayMinX


image = cv2.imread( "cat.jpg" , 0)

shapeArray = getShape( image )

