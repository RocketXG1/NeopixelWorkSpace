# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from machine import Pin
from NeoPixel.neopixel import Neopixel
from NeoPixel.BlackLight.BlackLightControl import BlackLightControl

numpix = 36
strip = Neopixel(numpix, 0, 29, "RGB")
Ready = Neopixel(1, 1, 16, "GRB")

bSensor=Pin(27,Pin.IN)

BlackLight=BlackLightControl(28,1000)


red = (255,0,0)
green = (0, 255,0)
blue = (0, 0, 255)

orange = (255, 50, 0)
yellow = (255, 150, 0)
cian = (0, 255, 255)
violet = (200, 0, 100)
wite= (120,120,120)
Off=(0,0,0)
colors_rgb = [red, orange, yellow, green, blue, cian, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
#colors = colors_rgb
colors = colors_rgbw





Ready.brightness(255)
Ready.fill(red)
Ready.show()
print("Ready")

iStartDelay=0.04
iFinishDelay=0.06
strip.brightness(255)
strip.fill(cian)
strip.show() 
print("Ready2")

iStartDelay=0.05
iFinishDelay=0.06

strip.circular_bounce_fill(wite,iStartDelay,iFinishDelay,150)
strip.animate_color_range(25,34,red,0.5,False)
strip.animate_color_range(0,35,Off,1,True) 

def MonStart():
    strip.circular_bounce_fill(wite,iStartDelay,iFinishDelay,150)
    strip.animate_color_range(25,34,red,0.5,False)    
    strip.animate_color_range(0,24,yellow,1.5,False)

def MonSleep():
    strip.animate_color_range(0,35,Off,1,True) 


Ready.brightness(200)
while True:  

    BlackLight.set_percent(50)     

   # if bSensor.value():
    #    Ready.fill(cian)
     #   MonStart()
        
    #else:        
     #   Ready.fill(green)
      #  Ready.show()
       # MonSleep()

    
        
    
    
   
    
    
    
    

    
    
    
