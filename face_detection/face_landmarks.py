import os
import dlib

_predictor_file = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "shape_predictor_68_face_landmarks.dat")
_predictor_points = 68

if not os.path.exists(_predictor_file):
    print "Shape predictor file not found."
    exit(1)

_predictor = dlib.shape_predictor(_predictor_file)


def landmarks(image, shape):
    image_h, image_w = image.shape[:2]
    return [(shape.part(i).x / float(image_w), shape.part(i).y / float(image_h)) for i in range(_predictor_points)]


def face_shape(image, rect):
    return _predictor(image, rect)
