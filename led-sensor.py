from machine import Pin, ADC
import time

ldr = ADC(Pin(26))         # LDR connected to GP26
led = Pin(15, Pin.OUT)     # LED connected to GP15
threshold = 9050           

try:
    while True:
        light = ldr.read_u16()
        print("Light level:", light)

        if light > threshold:     # BRIGHT
            led.off()
            print("Bright – LED OFF")
        else:                     # DARK
            led.on()
            print("Dark – LED ON")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped.")
