FROM ubuntu:latest

RUN apt-get update && apt-get install -y python-pip wget bzip2 python-dev cmake zip libboost-all-dev

COPY . /app

WORKDIR /app/face_detection/data
RUN chmod +x models.sh && ./models.sh

WORKDIR /app
RUN pip install -r requirements.txt

RUN  apt-get install -y libsm6 libxext6 libfontconfig1 libxrender1

EXPOSE 5000

CMD [ "python", "server.py" ]