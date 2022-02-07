import flask
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import Adafruit_DHT

SCHEDULER = BackgroundScheduler()
APP = flask.Flask(__name__)

timestamp = None
humidity = None
temperature = None
sensor_communicating = True

try:
    DHT_SENSOR = Adafruit_DHT.DHT22
except:
    sensor_communicating = False

# The GPIO pin that links to the data pin on your DHT sensor.
DHT_PIN = 3

def getReadings():
    global humidity, temperature, timestamp
    try:
        # Gather readings from the sensor.
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    else:
        humidity = False
        temperature = False
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Schedule the first refresh in 5 seconds.
SCHEDULER.add_job(func = getReadings, trigger = "interval", seconds = 5)
SCHEDULER.start()

@APP.route('/')
def hello():
    global humidity, temperature, timestamp
    return flask.jsonify(
        timestamp = timestamp,
        temperature = temperature,
        humidity = humidity
    )

if __name__ == "__main__":
    APP.run(host = "0.0.0.0", port = '4000', debug = True)