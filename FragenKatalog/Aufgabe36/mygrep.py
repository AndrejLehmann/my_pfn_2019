import re

def mygrep(pattern, inputfile):
    with open(inputfile,'r') as f:
        for line in f:
            m = re.search(pattern, line)
            if m:
                print(line, end = '')

mygrep('\d+', 'test.txt')
