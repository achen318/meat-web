from flask import Flask

# import os

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


# app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'
# app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}


# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return 'No file part', 400

#     image_file = request.files['image']
#     if image_file.filename == '':
#         return 'No selected file', 400

#     if image_file and allowed_file(image_file.filename):
#         filename = secure_filename(image_file.filename)
#         image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return 'Image uploaded successfully!', 200
#     else:
#         return 'Invalid file type', 400


# if __name__ == '__main__':
#     app.run(debug=True)
