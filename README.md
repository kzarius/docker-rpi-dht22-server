# docker-rpi-dht22-server

This small package uses a Raspberry Pi Zero W with an attached Adafruit DHT22 humidity and temperature sensor. It uses Python to grab the sensor data and broadcast on port 4000.

## Usage

Enable the I2C interface by running `sudo raspi-config` and navigating into `Interface Options` > `I2C`.

By default, GPIO pin 3 is to be used for the DATA pin, but can be adjusted in `sensor.py`. Change your outward port in `docker-compose.yml` if you need to, and ensure you have docker / docker-compose. Run the docker-compose.yml file by cd'ing to the directory and running `docker-compose up -d --build`.

You should now begin to see the JSON replies broadcasted at `http://localhost:4000`