# Pi Remote CAR

This is a DIY project for a Pi Car hobbyist (estimated build time - 1 week)

## Architecture

<img src="https://d3ansictanv2wj.cloudfront.net/Figure_1-1ad2b142be6ca8641212c7579ab4f95d.jpg" height="400">


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

## Step 3: Connect Pi and other sensors

TODO Hook up a Pi Zero to control as main processing unit and control of other cars components 

## Step 4,5,6,7 TODO
* Add camera and Tensorflow for AI and image recongnition (http://elinux.org/RPi-Cam-Web-Interface)
```
    git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
    cd RPi_Cam_Web_Interface
    chmod u+x *.sh
    ./install.sh
```
* Add Web Interface
 * install Nginx
 * Build a simple Python webserver
* Add Sensors for Collision avoidance
 * <img src ="http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/12/Ultrasonic-Sensor-03.jpg" height="120">
* Add Temperature Sensors to follow heat signatures
