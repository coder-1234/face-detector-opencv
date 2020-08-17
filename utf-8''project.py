#!/usr/bin/env python
# coding: utf-8
##BEGINING OF ACTIUAL CODE
# In[18]:


from zipfile import ZipFile
from PIL import Image
import pytesseract as ts
images = {}
zf= ZipFile('readonly/small_img.zip')
for i in zf.infolist():
    img = Image.open(zf.open(i.filename))
    images[i.filename] = ts.image_to_string(img).replace('\n',' ')


# In[1]:


print(images)


# In[16]:


import numpy as np
import cv2 as cv
import math
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
for i in zf.infolist():
    if 'Christopher' in images[i.filename]:
        print('Results found in file',i.filename)
        img = Image.open(zf.open(i.filename))
        cv_img = np.array(img)
        faces = (face_cascade.detectMultiScale(cv_img,1.35)).tolist()
        if len(faces)>0:
            contact_sheet = Image.new(img.mode,(500, 100*math.ceil(len(faces)/5)))
            xaxis = 0
            yaxis = 0
            for x,y,w,h in faces:
                new_img = img.crop((x,y,x+w,y+h))
                new_img.thumbnail((100,100))
                contact_sheet.paste(new_img,(xaxis,yaxis))
                if xaxis+100 == contact_sheet.width:
                    xaxis=0
                    yaxis=yaxis+100
                else:
                    xaxis=xaxis+100

            display(contact_sheet)
        else: print('But there were no faces in that file')

## END OF ACTUAL CODE

#     ## EXTRA CODES ONLY FOR TESTING OF MODULES

# In[15]:

## TESTING FOR DIFFERENT VALUES OF SCALE FACTOR TO RECIEVE CORRECT OUTPUTS

from zipfile import ZipFile
from PIL import Image
import numpy as np
import cv2 as cv
zf= ZipFile('readonly/small_img.zip')
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
img = Image.open(zf.open('a-2.png'))
cv_img = np.array(img)
faces = (face_cascade.detectMultiScale(cv_img,1.35)).tolist()
print(len(faces))


# In[17]:

## TESTING FOR DISPLAY MODULE
faces = []
img = Image.open(zf.open('a-2.png'))
contact_sheet = Image.new(img.mode,(500, 0))
xaxis = 0
yaxis = 0
for x,y,w,h in faces:
    new_img = img.crop((x,y,x+w,y+h))
    new_img.thumbnail((100,100))
    contact_sheet.paste(new_img,(xaxis,yaxis))
    if xaxis+100 == contact_sheet.width:
        xaxis=0
        yaxis=yaxis+100
    else:
        xaxis=xaxis+100


# In[14]:


display(contact_sheet)


# In[ ]:




