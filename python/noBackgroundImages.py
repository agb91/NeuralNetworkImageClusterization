# import the necessary packages
import cv2
import sys
import os
from os import walk

#read image names in a folder
def readImagesNames( folder ):
	f = []
	for (dirpath, dirnames, filenames) in walk(folder):
		f.extend(filenames)
		break
	return f	

#get all images in a folder, as an array
def loadAllImagesFromFolder( folder ):
    images = []
    for filename in os.listdir( folder ):
        img = cv2.imread( os.path.join( folder , filename ) )
        if img is not None:
            images.append( img )
    return images

#resize all images given
def resizeImages( images , dim ):
	newImages = []
	for img in images:
		img = cv2.resize( img , ( dim , dim ) )
		if img is not None:
			newImages.append( img )
	return newImages

def cleanDirectory( path ):
	fileList = os.listdir( path )
	for fileName in fileList:
		os.remove( path + "/" + fileName )


#write an array of images in a path
def writeAllImages( path , images ):
	cleanDirectory( path )
	i = 0
	for img in images:
		name = str ( i ) + ".jpg"
		cv2.imwrite( path + "/" + name , img )
		i+=1

def discardImagesWithBackground( images ):
	newImages = []
	for img in images:
		px = img[ 1 , 1 ]
		if ( img[ 1 , 1 ] > ( 235 , 235 , 235 ) ).all():
			newImages.append( img )	
	return newImages	


print 'setted path: ' , str( sys.argv[1] )
path = sys.argv[1]
images = loadAllImagesFromFolder( path )
images = discardImagesWithBackground( images )
print 'number of read images: ' + str( len( images ) )
writeAllImages ( path , images )
