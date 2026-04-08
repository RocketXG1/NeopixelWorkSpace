# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from NeoPixel.neopixel import Neopixel
#from BlackLight.BlackLightControl import BlackLightControl

numpix = 36
strip = Neopixel(numpix, 0, 29, "RGB")
Ready = Neopixel(1, 1, 16, "GRB")

#BlackLight=BlackLightControl(28,1000)


red = (255,0,0)
green = (0, 255,0)
blue = (0, 0, 255)

orange = (255, 50, 0)
yellow = (255, 150, 0)
indigo = (100, 0, 90)
violet = (200, 0, 100)
wite= (120,120,120)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
#colors = colors_rgb
colors = colors_rgbw



iStartDelay=0.03
iFinishDelay=0.06

Ready.brightness(255)
Ready.fill(red)
Ready.show()
print("Ready")

iStartDelay=0.03
iFinishDelay=0.06
strip.brightness(255)
strip.fill(indigo)
strip.show() 
print("Ready2")
strip.circular_bounce_fill(wite,iStartDelay,iFinishDelay,255)
while True:
    Ready.brightness(255)
    Ready.fill(green)
    Ready.show()

    strip.set_pixel_line(20,5,red,colors_rgbw[0])
    strip.show()
    
    iStartDelay=0.03
    iFinishDelay=0.06     
    
    
    
    

    
    
    
