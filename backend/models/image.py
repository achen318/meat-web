from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import os

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier =load_model('image_model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

TRACEY_HAPPY = cv2.imread('IMG_5251.JPG')


def analyze_img(img):
    import cv2
import numpy as np

def analyze_img(img):

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_classifier.detectMultiScale(gray)

    predicted_emotions = []

    # Iterate through detected faces
    for (x, y, w, h) in faces:
        # Extract ROI (region of interest) for face
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        # Normalize and preprocess ROI
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = np.expand_dims(roi, axis=0)

            # Predict emotion using the CNN model
            prediction = classifier.predict(roi)[0]
            label = emotion_labels[prediction.argmax()]
            predicted_emotions.append(label)
        else:
            predicted_emotions.append('No Face Detected')

    return predicted_emotions

# Example usage:
# img = cv2.imread('path/to/image.jpg')
# predicted_emotions = analyze_img(img)
# print(predicted_emotions)

print(analyze_img(TRACEY_HAPPY))






# take in image, return emotions and confidence levels
