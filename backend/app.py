from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


@app.route("/img-rec")
def img_rec():
    # does stuff w img w machine learnin
    emotion = "happy"
    confidence = 0.9

    return {"confidence": confidence, "emotion": emotion}
