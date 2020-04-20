#!/bin/sh

set -e -x
if test $# -eq 1
then
  echo "Usage: $0 py|rb <inputfile>"
  exit 1
fi
sf=$1
shift
for filename in $*
do
  this_filename=`echo ${filename} | sed -e 's/@$//'`
  cat $this_filename | newick_parse.${sf} -n - | diff - $this_filename
done
