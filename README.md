# Face Detector
Simple Flask and docker-ready application as a server to detect faces, genders and their landmarks.

### Docker

```bash
$ docker pull ahmdrz/facedetector:latest
$ docker run -p 5000:5000 ahmdrz/facedetector:latest
```

#### Sample

**Request**

```bash
$ curl "localhost:5000/detect?gender=on&url=https://pixel.nymag.com/imgs/daily/vulture/2018/09/04/04-eminem-2.w700.h700.jpg
```

**Response**

```json
{
  "result": [
    {
      "box": [
        0.3375,
        0.115,
        0.2275,
        0.2275
      ],
      "gender": "male",
      "index": 0,
      "landmarks": [
        [
          0.36,
          0.1875
        ],
        [
          0.3625,
          0.21
        ],
        [
          0.365,
          0.2325
        ],
        ... // there are 68 points...
      ],
      "score": 0.43
    }
  ],
  "status": "ok"
}
```

### Dependencies

First of all , clone this repository using `git clone https://github.com/ahmdrz/facedetector`.

To install all of dependencies run `sudo pip install -r requirements.txt` , after installing python packages , you have to download pre-trained dlib models.

```
  cd face_detection/data
  ./models.sh
```

### How to use in clients ?

See `example.py` for details.

This small application has only one route , `/detect`.

Optional query parameters is `landmarks` and `gender`. Use `landmarks=on` to detect 68 point of face landmarks. Use `gender=on` to predict face gender.

You can use `url` query parameter.

Curl examples :

```bash
$  curl "localhost:5000/detect?url=<picture url>"
$  curl -F "image=@<picture file path>" "localhost:5000/detect?landmarks=on"
$  curl -F "image=@<picture file path>" "localhost:5000/detect?gender=on"
```

**Note**: All of the cordinates in this application is based of `image width` and `image height`.

#### Keywords

1. Docker face detection
2. Docker face gender detector
3. Docker face landmarks