# AD9833-Pi-Pico-MicroPython

A small class to control the AD9833 DDS chip using the Pi Pico in micropython

# Usage 
```Python
DriveFreq = 129000
ad9833 = AD9833()
ad9833.change_freq(DriveFreq)
ad9833.set_sine()
```


Based on the comment by horuable in https://forums.raspberrypi.com/viewtopic.php?t=306297