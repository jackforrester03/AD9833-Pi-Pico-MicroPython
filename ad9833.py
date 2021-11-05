from machine import Pin, SPI
from time import sleep

class AD9833:
    def __init__(self, sckPin = 18, misoPin=16, mosiPin=19, csPin=17):
        self.spi = SPI(0, baudrate = 1000000, sck = Pin(sckPin, Pin.OUT),
                      miso = Pin(misoPin, Pin.OUT), mosi = Pin(mosiPin, Pin.OUT),
                      polarity = 1, phase = 1)

        self.cs = Pin(csPin, Pin.OUT)
        self.cs.value(1)
        self.MCLK = 25*10**6
        self.reset()

    def reset(self):
        self.cs.value(0)
        self.spi.write(bytes([0x01, 0x00]))
        sleep(0.01)
        self.spi.write(bytes([0x20, 0x00]))
        self.cs.value(1)

    def convert_freq(self, freq):
        tmp = int(freq*2**28/self.MCLK)
        return bytes([tmp >> 8 & 0x3f | 0x1 <<6, tmp & 0xff,
                tmp >> 22 | 0x1 << 6, tmp >> 14 & 0xff])

    def change_freq(self, freq):
        self.cs.value(0)
        self.spi.write(self.convert_freq(freq))
        self.cs.value(1)

    def change_function(self, fun):
        '''
        Changes output function.
        Valid values to pass to this function are:
        0 - sine
        2 - triangle
        40 - square
        32 - square (half frequency)
        '''
        self.cs.value(0)
        # Setting the control register
        # 0x20 
        # - sets the B2B bit high to allow frequnecies to be loaded in
        # - No reset, using FREQ0 ande PHASE0 registers, HLB is ignoored

        # 0x??
        # The choice of number above will set the OPBITEN, DIV2 and the Mode registers
        # to give the desired output waveform 
        self.spi.write(bytes([0x20, fun]))
        self.cs.value(1)
        
    def set_sine(self):
        self.change_function(0)
        
    def set_square(self):
        self.change_function(40)
    
    def set_triangle(self):
        self.change_function(2)

