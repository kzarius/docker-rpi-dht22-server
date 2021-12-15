import redis
import time
import datetime
import sched
import Adafruit_DHT

REPEATER = sched.scheduler(time.time, time.sleep)
CACHE = redis.Redis(host='redis', port=6379)

DHT_SENSOR = Adafruit_DHT.DHT22
# The GPIO pin that links to the data pin on your DHT sensor.
DHT_PIN = 3

def getReadings(repeater_obj):
    # Gather readings from the sensor.
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Only write to redis if the sensor returns readings.
    if humidity is not None and temperature is not None:
        CACHE.update({
            "timestamp":str(datetime.datetime.now()).split('.')[0],
            "temperature":temperature,
            "humidity":humidity
        })

    # Schedule another refresh in 5 seconds.
    REPEATER.enter(5,1,getReadings,(repeater_obj,))

# Schedule the first refresh in 5 seconds.
REPEATER.enter(5,1,getReadings,(REPEATER,))
REPEATER.run()