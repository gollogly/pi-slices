#Using I2C to control servos, LEDs and use PWM
#Setup

import i2c
servos = i2c.I2C()
#leds = i2c.I2C(frequency=1000)
=The i2c class will by default set frequency to 50Hz to work well with servo pulses. If you don’t want to drive servos you can set it between 40 and 1000Hz to give more control and avoid flicker.

#Setting Speeds

servos.setSpeeds(100,-100)
#this will set the left motor (on led0) to full speed, and right motor (led1) to full reverse
servos.setSpeeds(50,50)
servos.setPWM(15,4095)
#this will set an LED on led15 to full brightness (on for 4095 ticks)
servos.setPWM(14,2048)  #set led14 to half brightness
