# pi-slices

## Pi Starter Projects

### Remote Access Project using VNC

* On your Pi (using a monitor or via SSH), install the TightVNC package

 ```
 sudo apt-get install tightvncserver
 tightvncserver
 ```

* Start a VNC server from the terminal: This example starts a session on VNC display one (:1) with full HD resolution: 

 ```
 vncserver :1 -geometry 1920x1080 -depth 24
 ```
 > Note that since by default an X session is started on display zero, you will get an error in case you use :0.

* Since there are now two X sessions running, which would normally be a waste of resources, it is suggested to stop the displaymanager running on

 ```
 service lightdm stop
 ```

* Now, on your computer, install and run the VNC client
 ``` 
 sudo apt-get install xtightvncviewer
 ```


# TODO

* Turn this into a script and run at boot

See https://www.raspberrypi.org/documentation/remote-access/vnc/ for more info
