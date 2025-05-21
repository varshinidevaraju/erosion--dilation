# EXP.9 Implementation-of-Erosion-and-Dilation
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
Dilate  the image

 
## Program:
NAME:VARSHINI D
REG NO:212223230234

###  Import the necessary packages
```py
import numpy as np
import cv2
import matplotlib.pyplot as plt
```
### Create the Text using cv2.putText
```py
img = np.zeros((100,400), dtype = 'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"SERENDIPITY",(5,70),font,2,(255,255,255),5,cv2.LINE_AA)
```
###  Create the structuring element
```py
kernel = np.ones((5,5),np.uint8)
kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
cv2.erode(img,kernel)
```
### Erode the image
```py
img_erode = cv2.erode(img,kernel1)
plt.imshow(img_erode)
plt.axis('off')

```
### Dilate the image
```py
img_dilate = cv2.dilate(img,kernel1)
plt.imshow(img_dilate)
plt.axis('off')
```
## Output:

### Display the input Image
![image](https://github.com/kanishka2305/erosion--dilation/assets/113497357/1df6e6a7-ac1e-41a1-9d43-b0d5ff2f6068)


### Display the Eroded Image
![image](https://github.com/kanishka2305/erosion--dilation/assets/113497357/13009d6b-57fe-4da0-8f04-738a65c0e611)


### Display the Dilated Image
![image](https://github.com/kanishka2305/erosion--dilation/assets/113497357/a0404c10-8e1b-49a1-a251-2a87626ecd00)


## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
