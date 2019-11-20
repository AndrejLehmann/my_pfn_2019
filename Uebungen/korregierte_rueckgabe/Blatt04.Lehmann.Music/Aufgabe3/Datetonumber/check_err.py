#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./datetonumber.py',1,
                    "Usage: ./datetonumber.py <inputfile with dates in format dd.mm.yyyy>")
mysubprocess_expect('./datetonumber.py xxx',1,
                    "./datetonumber.py: [Errno 2] No such file or directory: 'xxx'")
