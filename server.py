from flask import Flask
from flask import request
from flask import jsonify

import logging
import tempfile
import shutil
import os
import time
from face_detection import face_detector, image_reader

app = Flask(__name__)

temporary_directory = tempfile.mkdtemp()


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "not ok", "message": "this server could not understand your request"})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "not found", "message": "route not found"})


@app.errorhandler(500)
def not_found(e):
    return jsonify({"status": "internal error", "message": "internal error occurred in server"})


@app.route('/detect', methods=['GET', 'POST'])
def detect_human_faces():
    if request.method == 'POST':
        if 'image' in request.files:
            f = request.files['image']
            unix_time = int(time.time())
            path = os.path.join(temporary_directory, '{}_{}'.format(unix_time, f.filename))
            f.save(path)

            image = image_reader.read_image(path, width=400)
            os.remove(path)
        elif request.data:
            image = image_reader.read_string(request.data)
    else:
        image_url = request.args.get('url')
        image = image_reader.read_url(image_url, width=400)

    landmarks = request.args.get('landmarks') == 'on'
    gender = request.args.get('gender') == 'on'

    faces = face_detector.detect(image, landmarks=landmarks, gender=gender)

    return jsonify({"status": "ok", "result": faces})


if __name__ == "__main__":
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    print "Starting server on http://localhost:5000"
    print "Serving ...",
    app.run()
    print "Finished !"
    print "Removing temporary directory ...",
    shutil.rmtree(temporary_directory)
    print "Done !"
