import cv2
import numpy as np

#1.Consider the image provided in previous lab. Transform the image as follows: 
#resize to twice of the original size, translated 30 pixels horizontally and 50 pixels 
#vertically, rotated by 45o clockwise
#
#img = cv2.imread('lena.png', 0)
#
#resizedTwice = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
#
#rows1,cols1 = resizedTwice.shape
#
#mask = np.float32([[1,0,30],[0,1,50]])
#translatedImg = cv2.warpAffine(resizedTwice,mask,(cols1,rows1))
#
#rows2, cols2 = translatedImg.shape
#
#M = cv2.getRotationMatrix2D((cols2/2,rows2/2),45,1)
#dst = cv2.warpAffine(translatedImg,M,(cols2,rows2))
#
#cv2.imshow('Lena', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#2.Consider the following image:
#Perform the following thresholding on the image: cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, 
#cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV. Provide your narration on the
#behavior of various types 

#img = cv2.imread('abstracted.jpg', 0)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#
#cv2.imshow('threshold1', thresh1)
#cv2.imshow('threshold2', thresh2)
#cv2.imshow('threshold3', thresh3)
#cv2.imshow('threshold4', thresh4)
#cv2.imshow('threshold5', thresh5)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#3.apply adaptive thresholding and Otsu binarization. Do you see any improvement 
#in the result? Explain your answer with proper reason.

#img = cv2.imread('lena.png', 0)
#img = cv2.medianBlur(img,5)
#
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#
#cv2.imshow('threshold2', th2)
#cv2.imshow('threshold3', th3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Consider the following image
#Apply various filters such as averaging, Gaussian and median. Which one gives better result?
#Explain your answer with proper reason

#Averaging
#img = cv2.imread('noisyLena.png', 0)
#avg = cv2.blur(img,(5,5))
#cv2.imshow('Averaging', avg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Gaussian Blurring
#img = cv2.imread('noisyLena.png', 0)
#gaussian = cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow('Gaussian', gaussian)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Median Blurring
#img = cv2.imread('noisyLena.png', 0)
#median = cv2.medianBlur(img,5)
#cv2.imshow('Median', median)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Bilateral Filtering
#img = cv2.imread('noisyLena.png', 0)
#bilateral = cv2.bilateralFilter(img,9,75,75)
#cv2.imshow('Bilateral', bilateral)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Consider the following image
#Applying erosion, dilation, opening and closing on the image. 
#Explain the behavior of the operators

#Erosian
#img = cv2.imread('men.png')
#kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(img,kernel,iterations = 1)
#cv2.imshow('Morphological Transformation', erosion)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Dilation
#img = cv2.imread('men.png')
#kernel = np.ones((5,5),np.uint8)
#dilation = cv2.dilate(img,kernel,iterations = 1)
#cv2.imshow('Morphological Transformation', dilation)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Opening
#img = cv2.imread('men.png')
#kernel = np.ones((5,5),np.uint8)
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#cv2.imshow('Morphological Transformation', opening)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Closing
#img = cv2.imread('men.png')
#kernel = np.ones((5,5),np.uint8)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('Morphological Transformation', closing)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Consider the following image
#Apply different derivative operators such as Sobel, Laplacian and Canny edge detection 
#on the image.

#img = cv2.imread('dave.png')

#Laplacian
#laplacian = cv2.Laplacian(img,cv2.CV_8U)
#cv2.imshow('laplacian', laplacian)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#SobelX
#sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
#cv2.imshow('SobelX', sobelx)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#SobelY
#sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
#cv2.imshow('SobelY', sobely)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Canny Detection
#canny = cv2.Canny(img,100,200)
#cv2.imshow('Canny', canny)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




























































