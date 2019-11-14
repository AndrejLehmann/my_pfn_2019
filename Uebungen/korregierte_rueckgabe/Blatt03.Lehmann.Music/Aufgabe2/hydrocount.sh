#!/bin/sh

if test $# -ne 1
then
  echo "Usage: $0 <inputfile>"
  exit 1
fi

inputfile=$1

for seq in `cat ${inputfile}`
do
  echo $seq;
  ./hydrocount.py $seq
done
