import matplotlib
import matplotlib.pyplot as plt

import cv2
import sys
import numpy as np
import os

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eyeCascade= cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

# Read the image
image = cv2.imread('lena.jpg', 0)

if image is None:
    raise ValueError('Image not found')

# Detect faces in the image
faces = faceCascade.detectMultiScale(image)

print('Found {} faces!'.format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), 255, 2)
    roi = image[y:y+h, x:x+w]

    eyes = eyeCascade.detectMultiScale(roi)
    for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh), 255, 2)


plt.figure()
plt.imshow(image, cmap='gray')
plt.show() 
