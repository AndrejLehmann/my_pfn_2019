#!/usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 1h

import sys, argparse

def cigarXevalargparse():
    p = argparse.ArgumentParser()
    p.add_argument('-c', '--cost', action='store_true',
                   help='show cost for each cigarXstring')
    p.add_argument('-i','--identity', action='store_true',
                   help='show identity for each cigarXstring')
    p.add_argument('inputfile', type=str,
                   help='specify input file')
    return p.parse_args()

if __name__ == "__main__":
  cigarXevalargparse()
