#!/usr/bin/env python3

import re

s = 'cruel world'
print(re.findall(r'\w+',s))
print(re.findall(r'...',s))
print(re.findall(r'(...)',s))
print(re.findall(r'(..)(..)',s))
