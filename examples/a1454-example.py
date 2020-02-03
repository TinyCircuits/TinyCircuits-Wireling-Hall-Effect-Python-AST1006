# A1454 Analog Hall Effect Sensor Example
# Prints the magnetic field in millitesla, and temperature in Celsius
# Written by: Laverena Wienclaw for TinyCircuits

import tinycircuits_wireling
import tinycircuits_a1454
import time

# Enable power to pi hat and wirelings
wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0) # Select port (0-3) labeled on the Pi Hat

# Sensor init
a1454 = tinycircuits_a1454.A1454()

while True:
    print("Mag: {} mT\nTemp: {} degC".format(a1454.readMag(), a1454.readTemp()))
    time.sleep(1)





