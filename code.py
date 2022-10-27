import board
import busio
import digitalio
import time

import paa5100ej
# Because SPI pins arent normalized on the pi,
# the Pi Pico doesnt supply this method, instead, we have to use:
#spi = board.SPI()

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

# Pi Pico Pin numbering is different:
#cs = digitalio.DigitalInOut(board.D4)

cs = digitalio.DigitalInOut(board.GP5)
cs.direction = digitalio.Direction.OUTPUT

oflow = paa5100ej.PAA5100EJ(spi, cs)
oflow.set_rotation(0)

tx = 0
ty = 0

while True:
    
    try:
        x, y = oflow.get_motion()
    except RuntimeError:
        continue
        
    tx += x
    ty += y
    
    print("Motion: {:03d} {:03d} x: {:03d} y {:03d}".format(x, y, tx, ty))
    time.sleep(0.01)
    
    
