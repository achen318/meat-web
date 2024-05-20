import random


def analyze_img(img):
    emotion = random.choice(
        ["angry", "disgust", "fear", "happy", "neutral", "sad", "suprise"]
    )
    confidence = random.random()

    return {"confidence": confidence, "emotion": emotion}


# take in image, return emotions and confidence levels
