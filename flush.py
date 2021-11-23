import board
import neopixel
import time 

NUMBEROFLEDS = 500
pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS)

for x in range(NUMBEROFLEDS):
    pixels[x] = (0,0,0)
    time.sleep(0.0005)

time.sleep(2)
print("Done")