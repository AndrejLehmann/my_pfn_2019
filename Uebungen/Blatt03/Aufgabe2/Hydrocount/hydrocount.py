#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:

    hydrophob = hydrophil = 0
    hydrophobe_saeuren = ['A','F','I','L','M','P','V','W']
    for amino in sys.argv[1]:
        for c in amino:
            if c in hydrophobe_saeuren:
                hydrophob += 1
            else:
                hydrophil += 1
    print("hydrophobic={}, hydrophilic={}".format(hydrophob,hydrophil))
else:    
    sys.stderr.write("Usage: {} <aminoacid sequence>\n".format(sys.argv[0]))

