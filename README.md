# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step1:
Import the necessary pacakages

### Step2:
Create the text using cv2.putText

### Step3:
Create the structuring element

### Step4:
Erode the image

### Step5:
Dilate the Image

 
## Program:
```
NAME:VARSHINI D
REG NO:212223230234

# Import the necessary packages

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create the Text using cv2.putText

##  Load the image

img1=np.zeros((100,700),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

# Create the text using cv2.putText

cv2.putText(img1,'VIGNESH V' ,(5,70),font,4,(255),2,cv2.LINE_AA)

# Create the structuring element

kernel1=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))


# Erode the image

img_dilate=cv2.dilate(img1,kernel1)
img_erode=cv2.erode(img1,kernel1)

# Dilate the image

plt.figure(figsize=(12, 5))
plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.subplot(1,3,2)
plt.imshow(img_dilate,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(img_erode,cmap='gray')
```
## Output:

### Display the input Image
![image](https://github.com/user-attachments/assets/fceaf68b-8ffd-4915-bd09-d6de1a69c272)


### Display the Eroded Image
![image](https://github.com/user-attachments/assets/e94f802f-f2a0-4471-b2da-d1f7a52b1d52)


### Display the Dilated Image
![image](https://github.com/user-attachments/assets/84c6e169-e574-4811-a50e-d56d58a31943)


## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
