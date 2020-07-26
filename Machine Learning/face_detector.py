import cv2, os
from random import randrange 

path = os.path.dirname(os.path.realpath(__file__))

trained_face_data = cv2.CascadeClassifier(path + '/haarcascade_frontalface_default.xml')

img = cv2.imread(path + '/Modi.jpg')

# grey_scaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(img)
# face_coordinates = trained_face_data.detectMultiScale(grey_scaled_img)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 6)

cv2.imshow('AayGupta\'s Face Detector', img)
# cv2.imshow('AayGupta\'s Face Detector', grey_scaled_img)
cv2.waitKey()

print('Face Detection')