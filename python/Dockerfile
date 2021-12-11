FROM arm32v6/python:3-alpine

WORKDIR /usr/src/app

# Install Python3 & the sensor library.
RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev
RUN pip3 install Adafruit_DHT

CMD [ "python", "./sensors.py" ]