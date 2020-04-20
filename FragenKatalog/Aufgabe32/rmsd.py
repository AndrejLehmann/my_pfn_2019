#!/usr/bin/env python3
import math
import sys

def rmsd(vvector, wvector):
    if len(vvector) != len(wvector):
        sys.stderr.write('{}: {}'.format(sys.argv[0], 'Die Listen v and w sind unterschiedlich lang.
                                                       Die Berechnung des Abstandes ist nicht moeglich.')
        sys.exit(1)
    summe = 0.
    for i in range(len(vvector)):
        summe += (vvector[i].x - wvector[i].x)**2 + (vvector[i].y - wvector[i].y)**2 + (vvector[i].z - wvector[i].z)**2
    return math.sqrt(1./len(vvector)*summe)

