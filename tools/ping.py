#!/usr/bin/python
import os

class bcolors:
  boneup = '\033[92m'
  bonedown = '\033[91m'
  endc = '\033[0m'

bone1 = "192.168.0.101"
bone2 = "192.168.0.102"
bone3 = "192.168.0.103"
bone4 = "192.168.0.104"
bone5 = "192.168.0.105"
bone6 = "192.168.0.106"
bone7 = "192.168.0.107"
bone8 = "192.168.0.108"
bone9 = "192.168.0.109"
bone10 = "192.168.0.110"
bone11 = "192.168.0.111"
bone12 = "192.168.0.112"

if os.system("fping -t 50 -q " + bone1) == 0:
  print bcolors.boneup + "Bone01 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone01 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone2) == 0:
  print bcolors.boneup + "Bone02 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone02 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone3) == 0:
  print bcolors.boneup + "Bone03 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone03 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone4) == 0:
  print bcolors.boneup + "Bone04 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone04 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone5) == 0:
  print bcolors.boneup + "Bone05 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone05 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone6) == 0:
  print bcolors.boneup + "Bone06 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone06 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone7) == 0:
  print bcolors.boneup + "Bone07 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone07 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone8) == 0:
  print bcolors.boneup + "Bone08 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone08 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone9) == 0:
  print bcolors.boneup + "Bone09 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone09 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone10) == 0:
  print bcolors.boneup + "Bone10 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone10 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone11) == 0:
  print bcolors.boneup + "Bone11 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone11 is down!" + bcolors.endc

if os.system("fping -t 50 -q " + bone12) == 0:
  print bcolors.boneup + "Bone12 is up!" + bcolors.endc
else:
  print bcolors.bonedown + "Bone12 is down!" + bcolors.endc

