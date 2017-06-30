### Libraries ###
import os
from sense_hat import SenseHat
from datetime import datetime
from time import sleep

### Logging Settings ###

## Files will be named by time and date. To customize filname,
## enter a filename here. 
FILENAME = ""

#### Variables ####

## Write_frequency is how often the program saves measurements to the file.
## ie. 1 would be save every measurement after it is taken as a line of data.
## 20 would be save 20 lines of data after taking 20 measurements

WRITE_FREQUENCY = 1 


# interval = how many seconds between readings. ie interval=10 would take a
#reading every 10 seconds

interval = 10




### Functions ###

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def file_setup(filename):
  header  =["cpu_temp","temp_h","temp_p","humidity","pressure",
  "mag_x","mag_y","mag_z",
  "timestamp"]

  with open(filename,"w") as f:
      f.write(",".join(str(value) for value in header)+ "\n")

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)

def get_sense_data():
      sense_data=[]

      output_string = ",".join(str(value) for value in sense_data)
      batch_data.append(output_string)

      sense_data.append(getCPUtemperature())
      sense_data.append(sense.get_temperature_from_humidity())
      sense_data.append(sense.get_temperature_from_pressure())
      sense_data.append(sense.get_humidity())
      sense_data.append(sense.get_pressure())
      
      mag = sense.get_compass_raw()
      mag_x = mag["x"]
      mag_y = mag["y"]
      mag_z = mag["z"]
      sense_data.extend([mag_x,mag_y,mag_z])

      sense_data.append(datetime.now())

      return sense_data

### Main Program ###
sense = SenseHat()
sense.clear()

batch_data= []

if FILENAME == "":
  filename = "SenseLog-"+str(datetime.now())+".csv"
else:
  filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)

while True:
  sleep(interval)

   #sleep(n) tells the program to pause for n seconds before taking another measurement
   #ie. sleep(60) will result in the program taking 1 set of measurements every 60 seconds.

  sense_data = get_sense_data()
  log_data()
  
   
  if len(batch_data) >= WRITE_FREQUENCY:
      print("Writing to file..")
      with open(filename,"a") as f:
          for line in batch_data:
              f.write(line + "\n")       
          batch_data = []

   


