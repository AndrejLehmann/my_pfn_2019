import sys

def keyvaluefiles2dict(filenames):
    dic = {}
    for fname in filenames:
        with open(fname) as f:
            for line in f:
                key_val = line.rstrip('\n').split(' ')
                key = key_val[0]
                val = key_val[1]
                if key not in dic.keys():
                    dic[key] = val
                else:
                    sys.stderr.write('Multiple key "{}" in {}\n'.format(key, fname))
                    exit(1)
    return dic

print(keyvaluefiles2dict(['test1.txt', 'test2.txt']))
