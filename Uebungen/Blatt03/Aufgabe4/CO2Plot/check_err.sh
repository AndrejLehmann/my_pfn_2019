#!/bin/sh

if test ! -f CO2_plot.pdf
then
  echo "$0: CO2_plot.pdf does not exist"
  exit 1
else
  echo "Congratulations. Test passed."
  echo "But please check that your own plot looks like CO2_plot_reference.pdf"
fi
