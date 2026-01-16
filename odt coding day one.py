from machine import Pin
import time

led1=Pin(4,Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(5,Pin.OUT)
led4=Pin(19,Pin.OUT)
buzz=Pin(21,Pin.OUT)
d=0.3
haha=0
counter=10

while(counter>haha):
    led1.on()
    buzz.on()
    time.sleep(d)
    buzz.off()
    led2.off()
    led3.off()
    led4.off()
    time.sleep(d)
    led1.off()
    led2.on()
    buzz.on()
    time.sleep(d)
    buzz.off()
    led3.off()
    led4.off()
    time.sleep(d)
    led1.off()
    led2.off()
    led3.on()
    buzz.on()
    time.sleep(d)
    buzz.off()
    led4.off()
    time.sleep(d)
    led1.off()
    led2.off()
    led3.off()
    led4.on()
    buzz.on()
    time.sleep(d)
    buzz.off()
    time.sleep(d)
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    buzz.off()
    counter=counter-1
    
led1.off()
led2.off()
led3.off()
    
    

