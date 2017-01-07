"""
Driver for enigma program.  Currently doesn't work due to
inheritance issue in Wheel.py
"""

from WheelSet import WheelSet


newSet = WheelSet("123456789")
message = newSet.encryptString("Hello world")
print(message)

#Reset newSet to original state by creating new instance
newSet = WheelSet("123456789")
message = newSet.encryptString(message)

#Supposed to read "Hello world."
print(message)
