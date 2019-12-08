#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.3h

# Punkte: 2/2
# Korrektur: LZ

import re

string = 'Hallo, World!'
print(string)
print(string[:-8])

mylist = [1,2,3,0,5,6]
mylist[3]=4
print(mylist)

if int("1") == 1:
  print("string represents integer value 1")

strlist = ["a", "b", "c"]
#print(strlist.join("\t"))
# ihr sollte die Funktion join nutzen, schau mal wie diese verwendet werden soll
print('{}\t{}\t{}'.format(strlist[0],strlist[1],strlist[2]))  # as wanted?

debts = {'Frank':100, 'Andreas':200}
print("Andreas: {}".format(debts["Andreas"]))

def myfunction(a, b=2, c=3):
  return a+b-c

print(myfunction(1,0,c=2))

print(myfunction(1))

mydict={'a':1, 'b':2, 'c': 3}
if 'a' in mydict:
  print("mydict has the key 'a'")

text="this is my text"
print("Text length: "+str(len(text)))

stream = open(__file__, "r") # open the source file
line=stream.readline()
stream.close()
print(line, end="")

if re.search(r'abc','abc'):
  print("regular expression works correctly")


def searchfour(alist):
  for value in alist:
    if value == 4:  # else returns None
      return True

if searchfour(mylist):
  print("Four was found in list")
else:
  print("Four was not found in list")

if 4 == 0:
  print("Four is equal to zero")
else:
  print("Four is not equal to zero")

def returnzerostring():
    return "zero"

print(returnzerostring())
