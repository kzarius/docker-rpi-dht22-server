# rpi-sensors-server

This small package uses a Raspberry Pi Zero W with an attached Adafruit DHT22 humidity and temperature sensor. It uses Python to grab the sensor data and broadcast on port 4000 via Node.js.

## Usage

Configure your data pin in `sensors.py`, change your outward port in `docker-compose.yml` if you need to, and esnure you have docker / docker-compose. Run the docker-compose.yml file by cd'ing to the directory and running `docker-compose up -d --build`.

You should now begin to see the JSON replies broadcasted at `http://localhost:4000`

## Database

As for now, the package uses a single file to share the information found in `db/readings.txt` between containers until I explore other methods.
