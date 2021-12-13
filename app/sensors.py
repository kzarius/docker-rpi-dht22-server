import time
import datetime
import sched
import Adafruit_DHT

repeater = sched.scheduler(time.time, time.sleep)

DHT_SENSOR = Adafruit_DHT.DHT22
# The GPIO pin that links to the data pin on your DHT sensor.
DHT_PIN = 3

def getReadings(repeater_obj):
    # Gather readings from the sensor.
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Only write to file if the sensor returns readings.
    if humidity is not None and temperature is not None:
        f = open("readings.txt", "w+")
        # Format the JSON.
        f.write('{{"timestamp":"{0}","temp":"{1:0.1f}","humidity":"{2:0.1f}"}}'.format(
            str(datetime.datetime.now()).split('.')[0],
            temperature,
            humidity
        ))
        f.close()

    # Schedule another refresh in 5 seconds.
    repeater.enter(5,1,getReadings,(repeater_obj,))

# Schedule the first refresh in 5 seconds.
repeater.enter(5,1,getReadings,(repeater,))
repeater.run()