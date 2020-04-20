#!/bin/sh

if test $# -ne 2
then
  echo "Usage: $0 <plot_option> <inputfile>"
  exit 1
fi

plot_opt=$1
inputfile=$2
echo "create ${plot_opt}.pdf"
./co2_stat_mn.py --${plot_opt} ${inputfile}
if test ! -f ${plot_opt}.pdf
then
  echo "plot for ${plot_opt}.pdf not created" 
  exit 1
fi
