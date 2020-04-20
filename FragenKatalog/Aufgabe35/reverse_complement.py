import sys

def reverse_complement(string):
    new_string = ''
    for c in string:
        if c == 'A':
            new_string += T
        elif c == 'C':
            new_string += G
        elif c == 'G':
            new_string += C
        elif c == 'T':
            new_string += 'A'
        else:
            sys.stderr.write('{} enthaelt einen ungueltigen Buchstaben.'.format(string))
            sys.exit(1)
        return new_string
