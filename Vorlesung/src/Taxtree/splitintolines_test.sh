#!/bin/sh

if test $# -lt 1
then
  echo "Usage: $0 <inputfiles>"
  exit 1
fi

for inputfile in $*
do
  echo "${inputfile}"
  TMPFILE=`mktemp TMP.XXXXXX` || exit 1
  cat ${inputfile} | sed -e 's/ //g' | tr -d '\n' > ${TMPFILE}
  echo "" >> ${TMPFILE}
  splitintolines.py ${TMPFILE} | diff - ${inputfile}
  rm ${TMPFILE}
done
