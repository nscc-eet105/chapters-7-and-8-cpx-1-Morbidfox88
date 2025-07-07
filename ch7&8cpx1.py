from adafruit_circuitplayground import cp
import time
import random

pattern = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def blackout():
    cp.pixels.fill((0, 0, 0))

while True:
    for pixel in pattern:
        cp.pixels[pixel] = pixel_color()

    time.sleep(0.5)

blackout()


