#!/bin/python3

import json
import os, sys
from sensors import growbme680, growbme280, growbmp280, grownosensor
from camera import camera
from specimen import specimen

if __name__ == "__main__":
    print("Starting growlab")

    config = {}
    try:
        with open("./config.json") as f:
            config = json.loads(f.read())
    except Exception as e:
        sys.stderr.write("Error: {}".format(e))
        sys.exit(1)

    print("Loaded config, saving images every {} seconds to {}".format( config["images"]["interval_seconds"], config["images"]["output_directory"]))

    sensor = None
    sensor_type = os.getenv("SENSOR_TYPE", "none")
    print("sensor type:",sensor_type);
    if sensor_type == "bme280":
        sensor = growbme280()
    if sensor_type == "bmp280":
        sensor = growbmp280()
    if sensor_type == "bme680":
        sensor = growbme680(config["sensors"]["oversample"])
    elif sensor_type == "none":
        sensor = grownosensor()

    readings = sensor.get_readings()
    print(readings)

    cam = camera(config["images"])
    frame = cam.get_frame()

    pwd = os.getcwd()
    output_path = pwd + "/html"

    try:
       os.mkdir(output_path)
    except:
       pass

    spec = specimen(config["text"], config["images"])
    spec.save_image("{}/image.jpg".format(pwd), frame, readings)

    spec.save_html("{}/image.jpg".format(pwd), output_path, readings)
