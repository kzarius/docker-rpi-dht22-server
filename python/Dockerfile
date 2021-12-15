FROM arm32v6/python:3-alpine

# Install Python3 & the sensor library.
RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev
RUN pip3 install Adafruit_DHT

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "sensors.py" ]