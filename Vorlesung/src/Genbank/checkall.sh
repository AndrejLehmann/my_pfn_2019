#!/bin/sh

set -e -x

if test $# -ne 1
then
  echo "Usage: $0 py|rb"
  exit 1
fi

sf=$1

TMPFILE=`mktemp TMP.XXXXXX` || exit 1
runall.sh ${sf} > ${TMPFILE}
diff -I ^==== ${TMPFILE} results.txt
rm -f ${TMPFILE}
