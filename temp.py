import os
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

cpu_temp = getCPUtemperature()
cpu_temp = float(cpu_temp)

temp_factor = 1.64771573604061

sense.set_rotation(180)

while True:
    temp = sense.get_temperature()    
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    print(cpu_temp)
    temp_calibrated = temp - ((cpu_temp - temp)/temp_factor)
    temp_calibrated = round(temp_calibrated,2)
    print(temp)
    temp = int(temp)
    print(temp)
    tempstr=str(temp_calibrated)
    print(temp_calibrated)

    
    sense.show_message("%s C  " % tempstr)
    humidity=round(humidity,1)
    humidity=str(humidity)
    print(humidity)
    sense.show_message("%s %% " % humidity)
    pressure = round(pressure,0)
    pressure = str(pressure)
    print("%s millibars  " % pressure)
    sense.show_message("%s millibars  " % pressure)
    
