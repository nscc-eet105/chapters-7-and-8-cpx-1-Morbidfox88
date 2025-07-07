from adafruit_circuitplayground import cp
import time
import random
#Chad Collard
#Chapter7&8 cpx
#7/7/2025

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

def blackout():
    cp.pixels.fill((0, 0, 0))

with open("pixelpattern.txt", "r") as pattern_file:
    pattern_string = pattern_file.readline().strip()
    pattern_list_of_strings = pattern_string.split(',')
    pattern = [int(pixel_index_str) for pixel_index_str in pattern_list_of_strings]

while True:
    cp.pixels.fill((0, 0, 0))
    time.sleep(.1)
    for pixel in pattern:
        cp.pixels[pixel] = pixel_color()
        time.sleep(1.0)
        cp.pixels[pixel] = (0, 0, 0)
        time.sleep(.1)
    blackout()
