#!/usr/bin/env python3
# Bearbeitungszeit: 3.5h

# bitte eure Namen angeben
# Punkte: 4/4 
# Korrektur: LZ

import sys
import numpy as np


def listofvectors_read(file_name):
    vectors = []
    with open(file_name,'r') as f:
        for line in f:
            v = eval(line)
            vectors.append(v)
    return vectors


def rmsd_evaluate(v_vector, w_vector):
    assert isinstance(v_vector,list)
    assert isinstance(w_vector,list)
    assert len(v_vector) == len(w_vector)
    result = 0
    for n in range(len(v_vector)):
        assert len(v_vector[n]) == 3  #wieso w_vector nicht überprüfen?
        result += (v_vector[n][0] - w_vector[n][0])**2
        result += (v_vector[n][1] - w_vector[n][1])**2
        result += (v_vector[n][2] - w_vector[n][2])**2
    result = np.sqrt(1.0/len(v_vector) * result)
    return result


def listofvectors_rmsd_print(listofvectors):
#in range besser bis len(listofvectors) -1, weil die Schritt 2 ist.
# bei n = len(listofvectors)-1 ist listofvectors[n+1] nicht mehr gültig.
    for n in range(0,len(listofvectors),2):
        v = listofvectors[n]
        w = listofvectors[n+1]
        rmsd = rmsd_evaluate(v,w)
        print('rmsd(vector{},vector{})={:.5f}'.format(n+1,n+2,rmsd))


listOfVectors = listofvectors_read('rmsd_input.csv')
listofvectors_rmsd_print(listOfVectors)
