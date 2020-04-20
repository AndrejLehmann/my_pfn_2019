#!/bin/sh

run() {
echo "========= $* ==========="
$*
if test $? -ne 0
then
  echo "failure: ${cmd}"
  exit 1
fi
}

if test $# -ne 1
then
  echo "Usage: $0 py|rb"
  exit 1
fi

sf=$1

run "gb2fasta.${sf} Record.gb"
run "gb2fields.${sf} Record.gb"
run "gb2annseq.${sf} Record.gb"
run "searchGB.${sf} Library.gb"
run "getAnno.${sf} Library.gb"
run "features.${sf} Library.gb"
run "gb_xml_parse.${sf}"
