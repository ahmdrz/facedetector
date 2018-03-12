# Face and Flask
Simple Flask application to detect faces, gender and their landmarks.

---
![Sample image](https://raw.githubusercontent.com/ahmdrz/face_and_flask/master/resources/image.jpg?raw=true)

### Dependency

First of all , clone this repository using `git clone https://github.com/ahmdrz/face_and_flask`.

To install all of dependencies run `sudo pip install -r requirements.txt` , after installing python packages , you have to download pre-trained dlib models (abote ~:

```
  cd face_detection/data
  ./models.sh
```

### Run server

This program used Flask as WSGI and router , to serve run `python server.py`.

### How to use in clients ?

See `example.py` for details.

This small application has only one route , `/detect`.

Optional query parameters is `landmarks` and `gender`. Use `landmarks=on` for detect 68 point of face landmarks. Use `gender=on` for predict face gender.

You can use `url` query parameter.

Curl examples :

```bash
  curl "localhost:5000/detect?url=https://raw.githubusercontent.com/ahmdrz/face_and_flask/master/resources/sample.jpg"
```

```bash
  curl -F "image=@resources/sample.jpg" "localhost:5000/detect"
```

```bash
  curl -F "image=@resources/sample.jpg" "localhost:5000/detect?gender=on"
```

Output example :

```json
{
  "result": [
    {
      "box": [
        0.3775, 
        0.5066666666666667, 
        0.2725, 
        0.36
      ], 
      "gender": "male",
      "index": 0.0, 
      "score": 2.4785936512483473
    }
  ], 
  "status": "ok"
}
```

**Note**: all of cordinates in this application is based of `image width` and `image height`.


#### TODO:

1. Create `/train` and `/guess` to train faces for face recognizer.
2. Use config file or command line arguments to modify server settings such as `Flask's listening port`.
