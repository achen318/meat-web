import cv2
from keras.models import load_model
import numpy as np

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
classifier = load_model("models/image_model.h5")

emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]


def analyze_img():
    img = cv2.imread("image.jpg")

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_classifier.detectMultiScale(gray)

    faces_emotions = []

    # Iterate through detected faces
    for x, y, w, h in faces:
        faces_emotions.append([])  # for each face

        # Extract ROI (region of interest) for face
        roi_gray = gray[y : y + h, x : x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        # Normalize and preprocess ROI
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype("float") / 255.0
            roi = np.expand_dims(roi, axis=0)

            # Predict emotion using the CNN model
            prediction = classifier.predict(roi)[0]
            for i, emotion in enumerate(emotion_labels):
                faces_emotions[-1].append((emotion, str(prediction[i])))

    # Sort emotions by confidence
    for face_emotions in faces_emotions:
        face_emotions.sort(key=lambda x: float(x[1]), reverse=True)
    return faces_emotions


# Example usage:
# img = cv2.imread('path/to/image.jpg')
# predicted_emotions = analyze_img(img)
# print(predicted_emotions)
