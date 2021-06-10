try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme680 import BME680
from bme280 import BME280
from bmp280 import BMP280

import time

class grownosensor:
    def __init__(self):
        pass

    def get_readings(self):
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
        }

class growbme680:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BME680()

    def get_readings(self):
#        temperature = self.sensor.get_temperature()
#        pressure = self.sensor.get_pressure()
#        humidity = self.sensor.get_humidity()
#        time.sleep(0.1)

#        temperature = self.sensor.get_temperature()
#        pressure = self.senor.get_pressure()
#        humidity = self.sensor.get_humidity()
        time_str = time.strftime("%H:%M:%S")
        self.sensor.get_sensor_data()
        temperature = self.sensor.data.temperature
        pressure = self.sensor.data.pressure
        humidity = self.sensor.data.humidity

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }

class growbme280:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BME280(i2c_dev=self.bus)

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }

class growbmp280:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BMP280(i2c_dev=self.bus)

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
        }
