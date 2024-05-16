import random

from PIL import Image
import cv2


def analyze_img(img):
    img = Image.frombytes("L", (3, 2), img)
    cv2.imshow("bruh", img)

    emotion = random.choice(
        ["angry", "disgust", "fear", "happy", "neutral", "sad", "suprise"]
    )
    confidence = random.random()

    return {"confidence": confidence, "emotion": emotion}


# take in image, return emotions and confidence levels
