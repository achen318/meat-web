from flask import Flask, request
from flask_cors import CORS

from models.image import analyze_img

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello world!"


@app.post("/img-rec")
def img_rec():
    img = request.data
    return analyze_img(img)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
