# Pi Remote CAR

This is a DIY project for a Pi Car hobbyist (estimated build time)

## Step 1: Get a Chassis and Build it (2-4 hours)

Remote Car usin Sain smart chassis and can be bought on Amazon or SainSmart website http://www.sainsmart.com/ for about £6

### Before

<img src="https://images-na.ssl-images-amazon.com/images/I/61qH18xAjVL._SL1200_.jpg" height="340" >

### After

<img src="pi-car-chassis-wired.jpg" height="340" >

## Step 2: Wire up (2-4 hours)

Hook up to a motor board to control the wheels. 

Starting with the a breadboard to write the motor functions (with design from fritzing)

<img src="raspberry-pi-connect-motor-board.png" height="240" >

See https://javatutorial.net/raspberry-pi-control-motor-speed
See https://www.youtube.com/watch?v=LwEBB6v559I

## Step 3: Connect Pi and other sensors

TODO Hook up a Pi Zero to control as main processing unit and control of other cars components 

## Step 4,5,6,7 TODO
* Add camera

  ```
  git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
  cd RPi_Cam_Web_Interface
  chmod u+x *.sh
  ./install.sh
  ```
* Add Tensorflow for AI and image recongnition
* Add Web Interface
* Add Sensors for Collision avoidance
  https://github.com/fivdi/pigpio
* Add Temperature Sensors to follow heat signatures
