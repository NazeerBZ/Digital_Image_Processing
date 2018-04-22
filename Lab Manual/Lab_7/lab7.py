import cv2
import numpy as np
from matplotlib import pyplot as plt

#1.Consider the image, Calculate the Fourier transform of the image and plot
#apply Laplacian, Gaussian and Sobel operator on the image. Now calculate the 
#Fourier transform of the processed image and plot it. What behavior do you see?

#img = cv2.imread('afridi.png',0)

#Fourier on Laplacian
#laplacian = cv2.Laplacian(img, cv2.CV_64F)
#plt.subplot(122),plt.imshow(laplacian, cmap = 'gray')
#plt.title('laplacian'), plt.xticks([]), plt.yticks([])
#plt.show()

#dft = cv2.dft(np.float32(laplacian),flags = cv2.DFT_COMPLEX_OUTPUT)
#dft_shift = np.fft.fftshift(dft)
#magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
#plt.title('Fourier'), plt.xticks([]), plt.yticks([])
#plt.show()

#Fourier on SobelX
#sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
#plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#plt.show()

#dft = cv2.dft(np.float32(sobelx),flags = cv2.DFT_COMPLEX_OUTPUT)
#dft_shift = np.fft.fftshift(dft)
#magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
#plt.title('Fourier'), plt.xticks([]), plt.yticks([])
#plt.show()


##Fourier on SobelY
#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
#plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
#plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.show()
#
#dft = cv2.dft(np.float32(sobely),flags = cv2.DFT_COMPLEX_OUTPUT)
#dft_shift = np.fft.fftshift(dft)
#magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
#plt.title('Fourier'), plt.xticks([]), plt.yticks([])
#plt.show()


#2.Find the position of head of the player in the image using the following template

#img = cv2.imread('afridi.png',0)
#template = cv2.imread('face.png',0)
#w, h = template.shape[::-1]
#
## Apply template Matching
#res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
## If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#top_left = min_loc
#bottom_right = (top_left[0] + w, top_left[1] + h)
#cv2.rectangle(img,top_left, bottom_right, 255, 2)
#
#plt.subplot(121),plt.imshow(res,cmap = 'gray')
#plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(img,cmap = 'gray')
#plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#
#plt.show()


#3.Consider the image
#Find the histogram of the image

#img = cv2.imread('flower.jpg',0)
#plt.hist(img.ravel(),256,[0,256])
#plt.show()


#4.Apply histogram equalization on the input image. Explain the behavior of 
#the equalization operation.

#equ = cv2.equalizeHist(img)
#cv2.imshow('Equalization',equ)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
