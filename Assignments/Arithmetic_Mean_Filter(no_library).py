import numpy as np
import cv2

image = cv2.imread('./images/hip-salt.jpg', 0);
width = image.shape[1]
height = image.shape[0]

result = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')

def meanFilter():    
  for row in range(height):
     for col in range(width):
         currentElement=0; left=0; right=0; top=0; bottom=0; topLeft=0; topRight=0; bottomLeft=0; bottomRight=0;
         counter = 1
         
#         print('Current Element', image[row][col])         
         currentElement = image[row][col]
         
         if not col-1 < 0:
#             print('left', image[row][col-1])
             left = image[row][col-1]
             counter +=1                        
         if not col+1 > width-1:
#             print('right',image[row][col+1])
             right = image[row][col+1]
             counter +=1 
         if not row-1 < 0:
#             print('top',image[row-1][col])
             top = image[row-1][col]
             counter +=1 
         if not row+1 > height-1:
#             print('bottom',image[row+1][col])
             bottom = image[row+1][col]
             counter +=1 
             
         if not row-1 < 0 and not col-1 < 0:
#             print('topLeft',image[row-1][col-1])
             topLeft = image[row-1][col-1]
             counter +=1 
         if not row-1 < 0 and not col+1 > width-1:
#             print('topRight',image[row-1][col+1])
             topRight = image[row-1][col+1]
             counter +=1 
         if not row+1 > height-1 and not col-1 < 0:
#             print('bottomLeft',image[row+1][col-1])
             bottomLeft = image[row+1][col-1]
             counter +=1 
         if not row+1 > height-1 and not col+1 > width-1:
#             print('bottomRight',image[row+1][col+1])
             bottomRight = image[row+1][col+1]
             counter +=1
             
         total = int(currentElement)+int(left)+int(right)+int(top)+int(bottom)+int(topLeft)+int(topRight)+int(bottomLeft)+int(bottomRight)
         avg = total/counter
         result[row][col] = avg

    
meanFilter(); 
cv2.imshow('Averaged', result);
cv2.imshow('Original', image);

cv2.waitKey(0)
cv2.destroyAllWindows()