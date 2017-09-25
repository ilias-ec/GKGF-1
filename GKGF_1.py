# Team Name: GKGF-1
# School Name: Gymnasium of Kanithos
# City: Chalkida
# Country: Greece
# Teacher: Economakos Elias (ICT) - ilias@sch.gr
# Style for Python Code: pep8online.com and pypi.python.org/pypi/pep8

# Libraries #
from sense_hat import SenseHat
from datetime import datetime
from time import strftime
from geopy.distance import vincenty
from geopy.distance import great_circle
import requests
import ephem
import time
import math
import os

# From: www.celestrak.com/NORAD/elements/stations.txt - the first 3 lines
# Last update: 25/2/2017
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   17055.97885185  .00018774  00000-0  28647-3 0  9996"
line2 = "2 25544  51.6412 237.6632 0006911 227.6655 268.1045 15.54462621 44303"

# Environmental data in ISS #
# From Environment Control and Life Support System (ECLSS):
#  wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf
# Cabin pressure nominal range: T = 14.2 to 14.9 psi
# 1 psi=68.9476 mbar - www.weather.gov/media/epz/wxcalc/pressureConversion.pdf
MIN_Pressure = round(14.2 * 68.9476, 4)  # = 979.0559 mbar
MAX_Pressure = round(14.9 * 68.9476, 4)  # = 1027.2769 mbar
# Cabin Temperature nominal range: T = 65 to 80 oF
# oC = (oF-32) * 5/9 - www.weather.gov/media/epz/wxcalc/tempConvert.pdf
MIN_Temperature = round((65 - 32) * 5.0/9.0, 4)  # = 18.3333 oC
MAX_Temperature = round((80 - 32) * 5.0/9.0, 4)  # = 26.6666 oC
# The cabin environment is usually maintained at about 60% relative humidity
# (corresponding to approximately 0.2 psi of water vapor pressure).
# www.faa.gov/other_visit/aviation_industry/designees_delegations/designee_types/ame/media/Section%20III.1.2%20Cabin%20Environment%20and%20EVA%20Environment.doc
# at page 12
MIN_Humidity = 50  # %relative humidity
MAX_Humidity = 70  # %relative humidity

# Logging Settings #
FILENAME = "GKGF_1_Greece"
FILENAME2 = "GKGF_1_Greece_calc"
WRITE_FREQUENCY = 10
# 3 hours x 60 min/hour x 60 sec/min = 10800 secs
#  plus 10 secs for the last circle
#  time.sleep(6) + 4 secs for delay of messages in 8x8 led display
PROGRAM_RUNNING_TIME = 10810


# Functions #
# Put data labels in file seperated by commas - 1st row
def file_setup(filename):
    header = ["date", "time",
              "temp_from_hum", "temp_from_pres", "humidity", "pressure",
              "cpu_tem",
              "pitch", "roll", "yaw",
              "pitch_rad", "roll_rad", "yaw_rad",
              "mag_North",
              "mag_x", "mag_y", "mag_z",
              "accel_x", "accel_y", "accel_z",
              "accel_x_raw", "accel_y_raw", "accel_z_raw",
              "gyro_x", "gyro_y", "gyro_z",
              "gyro_x_raw", "gyro_y_raw", "gyro_z_raw"]
    with open(filename, "w") as f:
        f.write(",".join(str(value) for value in header) + "\n")


# Put comma to separate data from sensors
def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)


# Data collection from sensors
def get_sense_data():
    sense_data = []
    # Date , Time
    sense_data.append(strftime("%d/%m/%Y"))
    sense_data.append(strftime("%H:%M:%S"))
    # Temperature from Humidity, Temperature from Pressure, Humidity, Pressure
    sense_data.append(sense.get_temperature_from_humidity())  # oC
    sense_data.append(sense.get_temperature_from_pressure())  # oC
    sense_data.append(sense.get_humidity())  # %rH
    sense_data.append(sense.get_pressure())  # mbar
    # CPU temperature
    res = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline()
    res = res.replace("\n", "")
    res = float(res)/1000  # oC
    sense_data.append(res)
    # Orientation
    o = sense.get_orientation()
    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch, roll, yaw])
    # Orientation in Radians
    o = sense.get_orientation_radians()
    yaw_rad = o["yaw"]
    pitch_rad = o["pitch"]
    roll_rad = o["roll"]
    sense_data.extend([pitch_rad, roll_rad, yaw_rad])
    # Compass - North
    mag_North = sense.get_compass()
    sense_data.extend([mag_North])
    # Compass - Raw
    mag = sense.get_compass_raw()
    mag_x = mag["x"]
    mag_y = mag["y"]
    mag_z = mag["z"]
    sense_data.extend([mag_x, mag_y, mag_z])
    # Accelerometer
    acc = sense.get_accelerometer()
    acc_x = acc["pitch"]
    acc_y = acc["roll"]
    acc_z = acc["yaw"]
    sense_data.extend([acc_x, acc_y, acc_z])
    # Accelerometer - Raw
    acc = sense.get_accelerometer_raw()
    acc_x_raw = acc["x"]
    acc_y_raw = acc["y"]
    acc_z_raw = acc["z"]
    sense_data.extend([acc_x_raw, acc_y_raw, acc_z_raw])
    # Gyroscope
    gyro = sense.get_gyroscope()
    gyro_x = gyro["pitch"]
    gyro_y = gyro["roll"]
    gyro_z = gyro["yaw"]
    sense_data.extend([gyro_x, gyro_y, gyro_z])
    # Gyroscope - Raw
    gyro = sense.get_gyroscope_raw()
    gyro_x_raw = gyro["x"]
    gyro_y_raw = gyro["y"]
    gyro_z_raw = gyro["z"]
    sense_data.extend([gyro_x_raw, gyro_y_raw, gyro_z_raw])
    return sense_data


# Put data labels in file separated by commas - 1st row
def file_setup2(filename2):
    header2 = ["date", "time", "latitude", "longitude", "altitude (m)"]
    with open(filename2, "w") as f:
        f.write(",".join(str(value2) for value2 in header2) + "\n")


# Put commas to separate data - timestamp, latitude, longitude, altitude
def log_data2():
    output_string2 = ",".join(str(value2) for value2 in sense_data2)
    batch_data2.append(output_string2)


# Data collection - timestamp, latitude, longitude, altitude
def get_sense_data2():
    sense_data2 = []
    # Timestamp
    sense_data2.append(strftime("%d/%m/%Y"))
    sense_data2.append(strftime("%H:%M:%S"))
    # ISS latitude and longitude
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    lat2string = str(tle_rec.sublat)
    lati = lat2string.split(":")
    if lati[0] == "-0" or float(lati[0]) < 0:
            # convert lat from dd:mm:ss to decimal - South hemisphere
            lati1 = float(lati[0])-float(lati[1])/60-float(lati[2])/3600
    else:
            # convert lat from dd:mm:ss to decimal - North hemisphere
            lati1 = float(lati[0])+float(lati[1])/60+float(lati[2])/3600
    long2string = str(tle_rec.sublong)
    longt = long2string.split(":")
    if longt[0] == "-0" or float(longt[0]) < 0:
            # convert long from dd:mm:ss to decimal - West hemisphere
            longt1 = float(longt[0])-float(longt[1])/60-float(longt[2])/3600
    else:
            # convert long from dd:mm:ss to decimal - East hemisphere
            longt1 = float(longt[0])+float(longt[1])/60+float(longt[2])/3600
    sense_data2.append(lati1)
    sense_data2.append(longt1)
    # ISS altitude
    sat = ephem.readtle(name, line1, line2)
    g = ephem.Observer()
    sat.compute(g)
    ISS_altitude = sat.elevation  # in meter
    sense_data2.append(ISS_altitude)

    return sense_data2


# Main Program #
sense = SenseHat()
# Enable the gyroscope, accelerometer and magnetometer
sense.set_imu_config(True, True, True)
#

batch_data = []
filename = FILENAME+"_"+datetime.now().strftime('%Y%m%d_%H%M%S')+".csv"
file_setup(filename)

batch_data2 = []
filename2 = FILENAME2+"_"+datetime.now().strftime('%Y%m%d_%H%M%S')+".csv"
file_setup2(filename2)

count_time_cycle = 0
Start_Time = time.time()  # Entry time program execution

while (time.time() - Start_Time) < PROGRAM_RUNNING_TIME:

    # ----- Write data from sensors and timestamp to file
    sense_data = get_sense_data()
    log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        with open(filename, "a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []
    # --------------------------------------------------
    # ----- Message to 8x8 led display when reach MIN/MAX
    #  for Temperature, Humidity, Pressure
    temperature_average = round((sense.get_temperature_from_humidity() +
                                 sense.get_temperature_from_pressure()) / 2, 4)
    if temperature_average >= MAX_Temperature:
        sense.show_message("MAX Temp",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    elif temperature_average <= MIN_Temperature:
        sense.show_message("MIN Temp",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    else:
        sense.show_message("Temp OK",
                           text_colour=[0, 255, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    if round(sense.get_humidity(), 4) >= MAX_Humidity:
        sense.show_message("MAX %rH",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    elif round(sense.get_humidity(), 4) <= MAX_Humidity:
        sense.show_message("MIN %rH",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    else:
        sense.show_message("%rH OK",
                           text_colour=[0, 255, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)

    if round(sense.get_pressure(), 4) >= MAX_Pressure:
        sense.show_message("MAX mbar",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    elif round(sense.get_pressure(), 4) <= MAX_Humidity:
        sense.show_message("MIN mbar",
                           text_colour=[255, 0, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    else:
        sense.show_message("mbar OK",
                           text_colour=[0, 255, 0],
                           back_colour=[255, 255, 255], scroll_speed=0.02)
    sense.clear()
    # --------------------------------------------------
    # ----- If possible a astronaut is near to Astro-Pi
    count_time_cycle += 1
    if count_time_cycle <= 7:
        temperature_average_initial = round((sense.get_temperature_from_humidity() +
                                             sense.get_temperature_from_pressure()) / 2, 4)
        humidity_initial = round(sense.get_humidity(), 4)
    if temperature_average > temperature_average_initial and round(sense.get_humidity(), 4) > humidity_initial:
        sense.show_message("Hi!",
                            text_colour=[0, 0, 255],
                            back_colour=[255, 255, 255], scroll_speed=0.05)
    sense.clear()
    # --------------------------------------------------
    # ----- Write data - timestamp, longitude, latitude and altitude to file
    sense_data2 = get_sense_data2()
    log_data2()

    if len(batch_data2) >= WRITE_FREQUENCY:
        with open(filename2, "a") as f2:
            for line in batch_data2:
                f2.write(line + "\n")
            batch_data2 = []
    # --------------------------------------------------
    time.sleep(6)  # + 4 secs for delay to display messages
                   # in 8x8 led display = 10 secs
f.close()
f2.close()
