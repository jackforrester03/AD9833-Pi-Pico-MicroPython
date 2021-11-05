# AD9833-Pi-Pico-MicroPython

A small class to control the AD9833 DDS chip using the Pi Pico in micropython

# Usage 
## Connection
The Pi Pico connects to the AD9833 over the SPI interface
* VCC -> 3.3V
* DGND -> GND
* SDATA -> GP19 (MOSI)
* SCLK -> GP18 (CLK)
* FSYNC -> GP17 (CS)
 
Custom pins can be provided in the class initaliser

## Waveform Output
To program the AD9833 to give a 10kHz sinusoidal output

```Python
from ad9833 import AD9833
DriveFreq = 10000
ad9833 = AD9833()
ad9833.change_freq(DriveFreq)
ad9833.set_sine()
```

A square wave output can be achieved using

```Python
ad9833.set_square()
```

A triangle wave output can be achieved using 

```Python
ad9833.set_triangle()
```

### 
<sup>This class is based on the comment by 'horuable' in https://forums.raspberrypi.com/viewtopic.php?t=306297<sup>