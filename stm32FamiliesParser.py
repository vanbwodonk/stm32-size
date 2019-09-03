#!/usr/bin/env python3
import xml.etree.ElementTree as ET
root = ET.parse('families.xml').getroot()
count = 0

def getMem(mcu):
      for Mcu in root.iter('Mcu'):
            RAMsize = 0
            FLASHsize = 0 
            if Mcu.attrib["RPN"] == mcu :
                  FLASHsize = int(Mcu.findtext("Flash"))
                  RAMsize= int(Mcu.findtext("Ram"))
                  break
      return FLASHsize, RAMsize
