#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


img1=np.zeros((100,700),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

cv2.putText(img1,'VARSHINI' ,(5,70),font,4,(255),2,cv2.LINE_AA)


# In[3]:


kernel1=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))


# In[4]:


img_dilate=cv2.dilate(img1,kernel1)
img_erode=cv2.erode(img1,kernel1)


# In[5]:


plt.figure(figsize=(12, 5))
plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.subplot(1,3,2)
plt.imshow(img_dilate,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(img_erode,cmap='gray')


# In[ ]:




