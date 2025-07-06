from adafruit_circuitplayground import cp
import time
import random

pixels_to_light = [0, 2, 4, 6, 8]

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def blackout():
    for pixel_index in pixels_to_light:
        cp.pixels[pixel_index] = (0, 0, 0)

while True:
    for pixel_index in pixels_to_light:
        cp.pixels[pixel_index] = pixel_color()
        time.sleep(1)

