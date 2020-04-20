#!/usr/bin/env python3

import re

def change_first_letter(w):
    _1st = w[0]
    w_ohne1st = w[1:]
    w_ohne1st = re.sub(_1st, '$', w_ohne1st)
    return _1st + w_ohne1st

for w in ['restart']:
    print('{} {}'.format(w, change_first_letter(w)))
