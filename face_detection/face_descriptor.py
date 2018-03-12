import dlib
import os

_face_model = dlib.face_recognition_model_v1(
    os.path.join(os.path.join(os.path.dirname(__file__), "data"), "dlib_face_recognition_resnet_model_v1.dat"))


def describe(image, shape):
    return _face_model.compute_face_descriptor(image, shape)
