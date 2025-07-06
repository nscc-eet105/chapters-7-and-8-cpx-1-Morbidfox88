from adafruit_circuitplayground import cp
import time
import random

# Chad Collard
# cpx6-1
# 6/27/2025

num_pixels = 10


def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def blackout():
    for i in range(num_pixels):
        cp.pixels[i] = (0, 0, 0)

while True:
    for pixel in range(num_pixels):
        cp.pixels[pixel] = pixel_color()
        time.sleep(0.01)


