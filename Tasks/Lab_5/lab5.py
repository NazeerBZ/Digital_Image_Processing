import cv2
import numpy as np

#1.	Consider the following image of model Lena. Load the image using Open CV and show on screen
#img = cv2.imread('lena.png', 0)
#cv2.imshow('Lena', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#2.	Create a border around the image
#img = cv2.imread('lena.png',1)
#constant = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_CONSTANT, value=[255,8,8])
#cv2.imshow('Lena', constant)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#3.	Create a copy of the face and paste it to the top right position
#img = cv2.imread('lena.png')
#face = img[80:167, 70:160]
#img[0:87, 0:90] = face 
#cv2.imshow('Lena', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#4.	Consider the following Pepsi logo. Blend it over the Lena’s image
#lena = cv2.imread('lena.png')
#pepsi = cv2.imread('pepsi.png')
#resizedPepsi = cv2.resize(pepsi, (220,220))
#dst = cv2.addWeighted(lena, 0.7, resizedPepsi, 0.3, 0)
#cv2.imshow('Lena', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#5.	Using bitwise AND, OR and NOT operators, paste the image of Pepsi on Lena’s image. 
#The background of Pepsi logo should not be pasted over, but only ROI will be pasted

#img1 = cv2.imread('lena.png')
#img2 = cv2.imread('pepsi.png')
#
#rows,cols,channels = img2.shape
#roi = img1[0:rows, 0:cols ]
#
#img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
#mask_inv = cv2.bitwise_not(mask)
#
#img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#
#img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
#
#dst = cv2.add(img1_bg,img2_fg)
#img1[0:rows, 0:cols ] = dst
#cv2.imshow('res',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#6.	Draw the following Olympic circles using Open CV.
#import numpy as np
#import cv2
#img = np.full((512,512,3), 255, np.uint8)
#blue =  cv2.circle(img,(140,123), 43, (255,8,8), 3)
#black =  cv2.circle(img,(240,123), 43, (0,0,0), 3)
#red =  cv2.circle(img,(340,123), 43, (2,0,253), 3)
#yellow =  cv2.circle(img,(187,163), 43, (24,252,242), 3)
#green =  cv2.circle(img,(290,163), 43, (9,109,61), 3)
#cv2.imshow('olympic',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()































