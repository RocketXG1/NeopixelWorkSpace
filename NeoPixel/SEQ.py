# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from NeoPixel.neopixel import Neopixel


def circular_bounce_fill(strip, color=(255, 0, 0), delay=0.05, brightness=50):
    numpix = strip.num_leds
    strip.brightness(brightness)
    off = (0, 0, 0, 0) if 'W' in strip.mode else (0, 0, 0)
    strip.fill(off)
    strip.show()

    left = 0
    right = numpix - 1
    previous = None
    while left <= right:
        strip.set_pixel(left, color)
        strip.set_pixel(right, color)
        if previous is not None:
            prev_left, prev_right = previous
            strip.set_pixel(prev_left, off)
            strip.set_pixel(prev_right, off)
        strip.show()
        time.sleep(delay)
        previous = (left, right)
        left += 1
        right -= 1

    left = max(left - 1, 0)
    right = min(right + 1, numpix - 1)
    while left > 0 or right < numpix - 1:
        if left > 0:
            left -= 1
            strip.set_pixel(left, color)
        if right < numpix - 1:
            right += 1
            strip.set_pixel(right, color)
        strip.show()
        time.sleep(delay)

numpix = 1
strip = Neopixel(numpix, 0, 16, "GRB")
# strip = Neopixel(numpsix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
#colors = colors_rgb
colors = colors_rgbw


step = round(numpix / len(colors))
current_pixel = 0
strip.brightness(5)

for color1, color2 in zip(colors, colors[1:]):
    strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
    current_pixel += step

strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)
print("Ready")
while True:
    #strip.rotate_right(1)
    #strip.fill(colors[2])
    #time.sleep(0.001)
    #strip.show()
    
    for Step in colors:
        strip.set_pixel(0,Step)
        #strip.fill(Step)
        time.sleep(0.1)
        strip.show()
        
    
    
    
