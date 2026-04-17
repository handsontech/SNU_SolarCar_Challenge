from mux04 import LineSensor
import time

sensor = LineSensor()

while True:
    channels = sensor.read_channels()
    print("channels : ", channels)
    time.sleep(0.1)
