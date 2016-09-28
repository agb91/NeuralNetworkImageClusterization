# import the necessary packages
import cv2
from sklearn.cluster import MiniBatchKMeans
import argparse
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")

#resize all images given
def resizeImages( images , dim ):
	newImages = []
	for img in images:
		img = cv2.resize( img , ( dim , dim ) )
		if img is not None:
			newImages.append( img )
	return newImages

def equalize( img ):
	equ = cv2.equalizeHist( img )
	return equ

def canny( img , low , high ):
	edges = cv2.Canny( img , low , high )
	return edges	

def quantizeColors( image , clustersNumber ):
	(h, w) = image.shape[:2]
	image = cv2.cvtColor( image, cv2.COLOR_BGR2LAB )
	 
	# reshape the image into a feature vector so that k-means
	# can be applied
	image = image.reshape( ( image.shape[ 0 ] * image.shape[ 1 ] , 3 ) )
	 
	# apply k-means using the specified number of clusters and
	# then create the quantized image based on the predictions
	clt = MiniBatchKMeans( n_clusters = clustersNumber )
	labels = clt.fit_predict( image )
	quant = clt.cluster_centers_.astype( "uint8" )[ labels ]
	 
	# reshape the feature vectors to images
	quant = quant.reshape( ( h , w , 3 ) )
	image = image.reshape( ( h , w , 3 ) )
	return quant
	# convert from L*a*b* to RGB
	#quant = cv2.cvtColor( quant , cv2.COLOR_LAB2BGR )
	#image = cv2.cvtColor( image , cv2.COLOR_LAB2BGR )
	#return quant

def segment( img ):
	ret,thresh = cv2.threshold( img , 127 , 255 , cv2.THRESH_TOZERO )
	return thresh


image = cv2.imread( 'test.jpg' )

#image = quantizeColors( image , 4 )

#image = equalize( image )
#image = canny( image , 250 , 450 )

#image = segment( image )
cv2.imwrite( 'output.jpg' , image )

cv2.waitKey(0)	