# import the necessary packages
import cv2
import sys
import os
import numpy as np
from os import walk
import math

def getArrayGrid( max , space ):
	ris = []
	howMany = int( math.floor( max / space ) )
	for x in range( howMany ):
		toAdd = x * space
		ris.append( toAdd )
	return ris

def checkAxisHorizontal( image , array , maxDim ):
	arrayMin = []
	arrayMax = []
	for x in array:
		thisMax = 0
		thisMin = maxDim - 1
		for y in range( maxDim ):
			if image[ y , x ] < 30:
				if y < thisMin:
					thisMin = y
				if y > thisMax:
					thisMax = y
		arrayMin.append( thisMin )
		arrayMax.append( thisMax )
	return arrayMin , arrayMax	

def checkAxisVertical( image , array , maxDim ):
	arrayMin = []
	arrayMax = []
	for x in array:
		thisMax = 0
		thisMin = maxDim - 1
		for y in range( maxDim ):
			if image[ x , y ] < 30:
				if y < thisMin:
					thisMin = y
				if y > thisMax:
					thisMax = y
		arrayMin.append( thisMin )
		arrayMax.append( thisMax )
	return arrayMin , arrayMax	

def printShape( arrayMaxY , arrayMinY , arrayMaxX , arrayMinX , h , w ):
	size = (w, h, channels) = (h, w, 1)
	img = np.zeros(size, np.uint8)
	img[ : ] = 255
	i = 0
	for x in getArrayGrid( w , 10 ):
		img[ x , arrayMinY[ i ] ] = 0
		img[ x , arrayMaxY[ i ] ] = 0
		i += 1
	i = 0	
	for y in getArrayGrid( h , 10 ):
		img[ arrayMinX[ i ] , y ] = 0
		img[ arrayMaxX[ i ] , y ] = 0
		i += 1	
	cv2.imwrite('output.jpg', img)

def normalize( array ):
	minimum = min( array )
	for i in range( len( array ) ):
		array[ i ] -= minimum 
	return array	
	
def getShape( image ):
	height, width = image.shape[:2]
	arrayWidth = getArrayGrid( width , 10 )
	arrayHeight = getArrayGrid( height , 10 )
	arrayMaxX = []
	arrayMinX = []
	arrayMaxY = []
	arrayMinY = []
	arrayMinX , arrayMaxX = checkAxisHorizontal( image , arrayWidth , height )
	arrayMinY , arrayMaxY = checkAxisVertical( image , arrayHeight , width )
	arrayMinX = normalize( arrayMinX )
	arrayMinY = normalize( arrayMinY )
	arrayMaxX = normalize( arrayMaxX )
	arrayMaxY = normalize( arrayMaxY )
	printShape( arrayMaxY , arrayMinY , arrayMaxX , arrayMinX , height , width)
	print arrayMaxY
	print arrayMinY
	print arrayMaxX
	print arrayMinX
	

image = cv2.imread( "bird.jpg" , 0)

shapeArray = getShape( image )

