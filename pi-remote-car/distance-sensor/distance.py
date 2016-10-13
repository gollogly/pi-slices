import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Set these for your specific ports
TRIG = 20
ECHO = 26

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()
  
while GPIO.input(ECHO)==1:
  pulse_end = time.time()
  
pulse_duration = pulse_end - pulse_start

# Take Speed of Sound / 2 is 17150 
distance = pulse_duration x 17150                 

distance = round(distance, 2)

print "Distance:",distance,"cm"

# Release GPIO connections
GPIO.cleanup()                                    