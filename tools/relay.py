#!/usr/bin/python

# The Rack System contains 12 Beaglebone Blacks, they are named Bone1 threw Bone12.
# Bone1 is the master node where this file will be executed to power up and down Bone2 threw bone12.
# the relays are wired to each of the pins p9_1 (DGND) and p9_9 (PWR_But) on bone2 threw bone12.
# Bone1 can not be cycled by this program.

#relay01="P8_8" (not used) (maybe case lights)
#relay02="P8_7"
#relay03="P8_10"
#relay04="P8_9"
#relay05="P8_12"
#relay06="P8_11"
#relay07="P8_14"
#relay08="P8_16"
#relay09="P8_15"
#relay10="P8_18"
#relay11="P9_12"
#relay12="P9_15"
#relay13="P9_23" (not used) (maybe fan for tier 1)
#relay14="P9_41" (not used) (maybe fan for tier 2)
#relay15="P9_27" (not used) (maybe fan for tier 3)
#relay16="P9_30" (not used) (maybe fan for tier 4)

# NAME
#  relay.py - simulates power button press or hold
# SYNOPSIS
#  relay.py [RELAY]... [MODE]...
# DESCRIPTION
#  -all
#    cycle threw all relays
#  -2
#    cycle relay #2
#  -3
#    cycle relay #3
#  -4
#    cycle relay #4
#  -5
#    cycle relay #5
#  -6
#    cycle relay #6
#  -7
#    cycle relay #7
#  -8
#    cycle relay #8
#  -9
#    cycle relay #9
#  -10
#    cycle relay #10
#  -11
#    cycle relay #11
#  -12
#    cycle relay #12
#  -p
#    press power button for one second
#  -h
#    hold power button for eight seconds (cannot be used with '-all')
# Example: to power up single Bone4
#    sudo python relay.py 4 -p
# Example: to power up all the bones
#    sudo python relay.py -all -p
# -h can not be used with -all

# Import the needed library's
import Adafruit_BBIO.GPIO as GPIO
import sys
from time import sleep

# pins used to control each of the relays
# Bone#     2       3        4       5        6        7        8        9       10       11       12
relay = ["P8_7", "P8_10", "P8_9", "P8_12", "P8_11", "P8_14", "P8_16", "P8_15", "P8_18", "P9_12", "P9_15"]
# Relay#    2       3        4       5        6        7        8        9       10       11       12

# setup relay pins used for Bones
for i in range(len(relay)):
   GPIO.setup ( relay[i], GPIO.OUT )
   GPIO.output ( relay[i], GPIO.HIGH )

# Simulate a one second button press for a single bone
if sys.argv[1].isdigit():
	if sys.argv[1] == "1":
		print "Error: you must use SSH to shutdown the master node."
		exit()
	if sys.argv[2] == "-p": # Button press
		GPIO.output(relay[int(sys.argv[1])-2], GPIO.LOW)
		sleep(1)
		GPIO.output(relay[int(sys.argv[1])-2], GPIO.HIGH)
	if sys.argv[2] == "-h": # Button hold
		GPIO.output(relay[int(sys.argv[1])-2], GPIO.LOW)
		sleep(8)
		GPIO.output(relay[int(sys.argv[1])-2], GPIO.HIGH)

# Simulate a one second button press across all eleven bones
if sys.argv[1] == "-all":
	if sys.argv[2] == "-h":
		print "Error: Illegal combo, please use -p instead"
		exit()
   if sys.argv[2] == "-p":
  	   for i in range(len(relay)):
  	   	GPIO.output(relay[i], GPIO.LOW)
  	   	sleep(1)
  	   	GPIO.output(relay[i], GPIO.HIGH)
  	   	sleep(5)

