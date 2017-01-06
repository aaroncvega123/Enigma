"""
Driver for enigma program.  Currently doesn't work due to
inheritance issue in Wheel.py
"""


newSet = WheelSet("12345679")
message = newSet.encryptString("Hello world")
print(message)
message = newSet.encryptString(message)

#Supposed to read "Hello world."
print(message)
