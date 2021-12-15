FROM arm32v6/python:3-alpine

# Install Python3 & dependencies.
RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip3 install -r requirements.txt

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "sensors.py" ]