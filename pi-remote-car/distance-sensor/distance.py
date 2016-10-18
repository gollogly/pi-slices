import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Set these for your specific ports
TRIG = 20
ECHO = 26

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():
  GPIO.output(TRIG, False)
  print "Waiting For Sensor To Settle"
  time.sleep(2)

  GPIO.output(TRIG, True)
  # set Trigger after 0.01ms to LOW
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  pulse_start = time.time()
	pulse_end = time.time()

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
  
  pulse_duration = pulse_end - pulse_start

  # Take Speed of Sound / 2 is 17150 
  distance = pulse_duration * 17150                 
  distance = round(distance, 2)
  print "Distance:",distance,"cm"
  
  return distance

# Release GPIO connections
if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print ("Measured Distance = %.1f cm" % dist)
			time.sleep(1)

		# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()                                  
