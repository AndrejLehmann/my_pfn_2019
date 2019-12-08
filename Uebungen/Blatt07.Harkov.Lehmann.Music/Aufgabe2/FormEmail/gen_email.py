#!/usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 2h

import sys
import re


with open(sys.argv[2],'r') as patientFile:
    patientLines = patientFile.readlines()

with open(sys.argv[1],'r') as emailTemplateFile:
    emailLines = emailTemplateFile.readlines()
emailLines = [l.rstrip('\n') for l in emailLines]


patientInfo = dict()
for line in patientLines:
    keyVal = re.search(r'^(_[A-Z]+_)\t(.+)$',line)
    key = keyVal.group(1)
    val = keyVal.group(2)
    patientInfo[key] = val


for line in emailLines:
    keyWord = re.findall(r'(_[A-Z]+_)',line) # multiple/no matches?
    if keyWord:
        for n in range(len(keyWord)):
            line = re.sub(keyWord[n],patientInfo[keyWord[n]],line)
    line = line.rstrip('\n')
    print(line)
