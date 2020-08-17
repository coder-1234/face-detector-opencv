from zipfile import ZipFile
from PIL import Image
import pytesseract as ts
import numpy as np
import cv2 as cv
import math

def face_finder(zipimages, name)
	images = {}
	zf= ZipFile(zipimages)
	for i in zf.infolist():
	    img = Image.open(zf.open(i.filename))
	    images[i.filename] = ts.image_to_string(img).replace('\n',' ')

	face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
	for i in zf.infolist():
	    if name in images[i.filename]:
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



face_finder('small_img.zip', 'Christopher')
face_finder('images.zip', 'Mark')
