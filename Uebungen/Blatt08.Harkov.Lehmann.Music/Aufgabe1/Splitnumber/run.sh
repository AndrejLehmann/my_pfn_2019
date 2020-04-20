#!/bin/sh

./splitnumber_mn.py 17 7 8
./splitnumber_mn.py 37 5 7
current_num=32
while test ${current_num} -ne 50
do
  ./splitnumber_mn.py ${current_num} 8 9
  ./splitnumber_mn.py ${current_num} 11 12
  ./splitnumber_mn.py ${current_num} 7 11 13
  current_num=`expr ${current_num} + 1`
done
