import re
import sys

def file2words(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except IOError as err:
        sys.stderr.write('{}: {}\n'.format(sys.argv[0], err))
        exit(1)

    words_dic = {}
    for line in lines:
        #                      v-- matches letters and _
        words = re.findall(r'(\w+)', line)
        for word in words:
            word = word.lower() # ignore case
            if word not in words_dic:
                words_dic[word] = 1
            else:
                words_dic[word] += 1

    return words_dic

print(file2words('poem.txt'))
