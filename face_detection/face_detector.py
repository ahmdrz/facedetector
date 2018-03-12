import dlib
import face_landmarks
import face_descriptor
import gender_detection

_detector = dlib.get_frontal_face_detector()


def detect(image, landmarks=False, gender=False, min_score=0.2):
    image_h, image_w = image.shape[:2]

    boxes, scores, idx = _detector.run(image, 1, -1)

    output = []
    for i, d in enumerate(boxes):
        if scores[i] < min_score:
            continue

        x, y, w, h = d.left(), d.top(), d.width(), d.height()
        x = x / float(image_w)
        y = y / float(image_h)
        w = w / float(image_w)
        h = h / float(image_h)
        face = {
            "box": [x, y, w, h],
            "score": scores[i],
            "index": idx[i],
        }
        if landmarks or gender:
            shape = face_landmarks.face_shape(image, d)

            if landmarks:
                face["landmarks"] = face_landmarks.landmarks(image, shape=shape)

            if gender:
                encoding = face_descriptor.describe(image, shape)
                face["gender"] = gender_detection.predict_gender(encoding=encoding)

        output.append(face)

    return output
