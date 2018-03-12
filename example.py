import cv2
from imutils.video import WebcamVideoStream
from imutils import resize
import requests


def detect(img, url='http://localhost:5000/detect?landmarks=on&gender=on'):
    _, img_encoded = cv2.imencode('.jpg', img)
    resp = requests.post(url, data=img_encoded.tostring())
    return resp.json()


camera = WebcamVideoStream(src=0).start()

while True:
    image = camera.read()
    image = resize(image, width=400)

    image_h, image_w = image.shape[:2]

    result = detect(image)
    if result["status"] == "ok":
        for face in result["result"]:
            x, y, w, h = face["box"]
            x, y, w, h = int(x * image_w), int(y * image_h), int(w * image_w), int(h * image_h)

            landmarks = face["landmarks"]
            for point in landmarks:
                point_x = int(point[0] * image_w)
                point_y = int(point[1] * image_h)
                cv2.circle(image, (point_x, point_y), 1, (200, 200, 100), -1)

            color = (0, 0, 255) if face["gender"] == "male" else (0, 255, 0)
            text = "gender: {}".format(face["gender"])
            text_width, text_height = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 0.75, 1)[0]
            cv2.rectangle(image, (x, y - text_height - 5), (x + text_width, y), color, -1)
            cv2.putText(image, text, (x, y - 3), cv2.FONT_HERSHEY_PLAIN, 0.75, (255, 255, 255))
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)

    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.stop()
