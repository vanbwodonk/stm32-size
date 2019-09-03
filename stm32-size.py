#!/usr/bin/env python3
import os
import subprocess
import re
import sys
from stm32FamiliesParser import getMem

print("STM32-size memory usage " + sys.argv[2])

MAXROM, MAXRAM = getMem(sys.argv[1])
MAXROM *=  1024
MAXRAM *=  1024
if MAXRAM == 0 or MAXROM == 0:
    print("Chip not found")
    sys.exit()

SIZEPROGREGEXP = r"^(?:\.text|\.data|\.rodata|\.text.align|\.ARM.exidx)\s+(\d+).*"
SIZEDATAREGEXP = r"^(?:\.data|\.bss|\.noinit)\s+(\d+).*"

cmdout = subprocess.Popen(
    ["arm-none-eabi-size", "-A", "-d", sys.argv[2]], stdout=subprocess.PIPE).communicate()[0]
cmdout = cmdout.decode('utf-8')
splitcmd = re.split(r'\s+', cmdout)
for i in range(0, len(splitcmd)):
    if splitcmd[i] == ".text":
        text = int(splitcmd[i+1])
    if splitcmd[i] == ".rodata":
        rodata = int(splitcmd[i+1])
    if splitcmd[i] == ".text.align":
        textalign = int(splitcmd[i+1])
    if splitcmd[i] == ".data":
        data = int(splitcmd[i+1])
    if splitcmd[i] == ".bss":
        bss = int(splitcmd[i+1])
    if splitcmd[i] == ".noinit":
        noinit = int(splitcmd[i+1])
ROMUSAGE = text + data + rodata
RAMUSAGE = bss + data
ROMPERCENT = ROMUSAGE / MAXROM * 100
RAMPERCENT = RAMUSAGE / MAXRAM * 100

print("FLASH usage : [", end="")
for i in range(1, 10):
    if ROMPERCENT / (i*10) >= 1:
        print("=", end="")
    else:
        print(" ", end="")
print("]  " + format(ROMPERCENT, '.1f') + "%", end="")
print("  (used " + str(ROMUSAGE) + " bytes from " + str(MAXROM) + " bytes)")
print("RAM usage   : [", end="")
for i in range(1, 10):
    if RAMPERCENT / (i*10) >= 1:
        print("=", end="")
    else:
        print(" ", end="")
print("]  " + format(RAMPERCENT, '.1f') + "%", end="")
print("  (used " + str(RAMUSAGE) + " bytes from " + str(MAXRAM) + " bytes)")
