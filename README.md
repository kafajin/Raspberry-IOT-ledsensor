# Raspberry-IOT-ledsensor

A Raspberry Pi Pico W project using an LDR to control an LED based on ambient light.

## 📌 Overview

This simple IoT-style project uses a Raspberry Pi Pico W with an LDR (light-dependent resistor) to measure light intensity and automatically turn an LED on or off depending on the brightness level. The project is written in MicroPython and run via Thonny IDE.

## 🧠 Objective

The goal is to understand how sensors can be used to control physical output devices like LEDs. This project demonstrates the basics of reading analog values and acting on them using conditional logic.

## ⚙️ Components Used

| Component                   | Quantity | Source       | Price (SEK) |
|----------------------------|----------|--------------|-------------|
| Raspberry Pi Pico W        | 1        | Elektrokit   | 89 SEK      |
| Breadboard                 | 1        | Elektrokit   | 69 SEK      |
| Jumper wires (male-male)   | 6        | Elektrokit   | 49 SEK      |
| LED (any color)            | 1        | Elektrokit   | 22 SEK      |
| Resistor (e.g., 330Ω)      | 1        | Included     | —           |
| LDR (photoresistor)        | 1        | Elektrokit   | 49 SEK      |
| Micro USB cable            | 1        | Elektrokit   | 19 SEK      |

## 🖥️ Software

- **Thonny IDE**
- **MicroPython firmware flashed on Raspberry Pi Pico W**

## 🔌 Wiring (Breadboard)

- **LDR:**
  - One leg to **3.3V** (red power rail)
  - Other leg to **GP26 (ADC0)** and **GND** via a resistor
- **LED:**
  - Long leg (anode) to **resistor** → then to **GP15**
  - Short leg (cathode) to **GND (blue rail)**

Ensure your power rails (red and blue lines on breadboard) are correctly connected to **3.3V** and **GND** from the Pico.

## 🧾 Code (main.py)

```python
from machine import Pin, ADC
import time

ldr = ADC(Pin(26))         # LDR connected to GP26
led = Pin(15, Pin.OUT)     # LED connected to GP15
threshold = 8900           # Adjust this threshold based on testing

try:
    while True:
        light = ldr.read_u16()
        print("Light level:", light)

        if light > threshold:
            led.off()
            print("Bright – LED OFF")
        else:
            led.on()
            print("Dark – LED ON")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped.")
🧪 Observations
In dark environments, the light level drops and the LED turns on.

In bright environments (e.g. flashlight), the level rises and the LED turns off.

Adjust threshold depending on ambient lighting.

📸 Final Setup 
https://drive.google.com/file/d/1T8vmLY0t6CtmtNryE7pxNTFPbl8X0so_/view?usp=sharing

📹 Video Demonstration
https://drive.google.com/file/d/12tpr0QtBMlIvqTTqOXQj4-Ct5T7pjZ6-/view?usp=sharing

💡 Improvements
Add OLED screen to display light level

Connect to WiFi and send values to a backend

Add Buzzer for alerts when it's too dark

🔗 License
MIT License © 2025
