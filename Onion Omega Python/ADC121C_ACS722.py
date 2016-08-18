# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADC121C_ACS722
# This code is designed to work with the ADC121C_I2CS_ACS722 I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# ADC121C_ACS722 address, 0x50(80)
# Select configuration register, 0x02(02)
#		0x20(32)	Automatic conversion mode enabled
i2c.writeByte(0x50, 0x02, 0x20)

time.sleep(0.5)

# ADC121C_ACS722 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# current MSB, current LSB
data = i2c.readBytes(0x50, 0x00, 2)

# Convert the data to 12-bits
current = (((data[0] & 0x0F) * 256) + data[1]) / 1000.0

# Output data to screen
print "Instantaneous Current value : %.6f A" %current
