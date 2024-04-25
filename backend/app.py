import random

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello world!"


@app.post("/img-rec")
def img_rec():
    # does stuff w img w machine learnin
    emotion = random.choice(
        ["angry", "disgust", "fear", "happy", "neutral", "sad", "suprise"]
    )
    confidence = random.random()

    return {"confidence": confidence, "emotion": emotion}
