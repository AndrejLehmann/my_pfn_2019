#!/usr/bin/env python3

from mysubprocess import mysubprocess_expect

mysubprocess_expect('./zahlenreihen.py',1,
                    "Usage: ./zahlenreihen.py <k>")
mysubprocess_expect('./zahlenreihen.py abc',1,
                    "./zahlenreihen.py: cannot convert 'abc' to int")
mysubprocess_expect('./zahlenreihen.py -3',1,
                    "./zahlenreihen.py: parameter -3 is not positive int")
