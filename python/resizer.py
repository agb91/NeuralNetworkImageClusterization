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

#write an array of images in a path
def writeAllImages( path , images ):
	names = readImagesNames( path )
	i = 0
	for img in images:
		name = names[i]
		cv2.imwrite( path + "/" + name , img )
		i+=1

#show the inputs, the chosen dimension and the path, and save them in variables
print 'set dimension (square): ', str( sys.argv[1] )
dim = int ( sys.argv[1] ) #parse int...
print 'set path: ' , str( sys.argv[2] )
path = sys.argv[2]

#read all the images in the folder 
images = loadAllImagesFromFolder( path )

#resize all of them
images = resizeImages( images , dim )

#write the new images on file
writeAllImages( path , images )

cv2.waitKey(0)
