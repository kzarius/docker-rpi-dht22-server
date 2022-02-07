import flask
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from smbus2 import SMBus

SCHEDULER = BackgroundScheduler()
APP = flask.Flask(__name__)

# Get the i2c object.
I2C_BUS = SMBus(1)

timestamp = None
humidity = None
temperature = None
sensor_communicating = True

try:
    I2C_BUS.write_i2c_block_data(0x44, 0x2c, [0x06])
except:
    sensor_communicating = False

def getReadings():
    global humidity, temperature, timestamp
    # Gather readings from the sensor.
    if sensor_communicating:
        SENSOR = I2C_BUS.read_i2c_block_data(0x44, 0x00, 6)
        humidity = 100 * (SENSOR[3] * 256 + SENSOR[4]) / 65535.0
        temperature = -45 + (175 * (SENSOR[0] * 256 + SENSOR[1]) / 65535.0)
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