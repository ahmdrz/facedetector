import dlib
import pickle
import os

_classifier = pickle.load(
    open(os.path.join(os.path.join(os.path.dirname(__file__), "data"), "gender_model.pickle"), 'r'))


# For train your own gender model visit:
# https://github.com/mrl-athomelab/ros-face-recognition#gender-detection

def predict_gender(encoding, threshold=0.5):
    result = _classifier(dlib.vector(encoding))
    if result > threshold:
        return "male"

    if result < -threshold:
        return "female"

    return "unknown"
