#!/usr/bin/env python3

import re, sys, random

s = 'abrcadabra'
for a in s:
  print('%{}'.format(a))

stream = list()
length_list = list()
for line in stream:
  length_list.append(len(line))

poem = 'Almost nothing was more'
char_list = list()
for cc in poem:
  if not (cc in char_list):
    char_list.append(cc)

for idx in range(25):
  print('%{}'.format(idx))

for idx, a in enumerate(s):
  print('%{}\t{}'.format(idx,a))

n = 10
for  i in range(1,n+1):
  for j in range(i+1,n+1):
    print('%{}\t{}'.format(i,j))

for  i in range(1,n+1):
  for j in range(0,i):
    print('%{}\t{}'.format(i,j))

s = '42'
try:
  i = int(s)
except ValueError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

'''
try:
  arg = sys.argv[1]
except KeyError as err:
  sys.stderr.write('Usage: {} <argument>\n'.format(sys.argv[0]))
  exit(1)

if len(sys.argv) < 2:
  sys.stderr.write('Usage: {} <argument>\n'.format(sys.argv[0]))
  exit(1)
'''

with open(__file__) as stream:
  for line in stream:
    length_list.append(len(line))

try:
  stream = open(__file__)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

lines = stream.readlines()
for line in lines:
  length_list.append(len(line))

for line in stream:  # better, as more space efficient
  length_list.append(len(line))

stream.close()

print('%',end='')
lss = ['a','b','c','d']
for i in range(len(lss)):
  s = '\t' if i < len(lss) - 1 else '\n'
  print('{}{}'.format(lss[i],s),end='')
print()

print('%',end='')
print('\t'.join(lss))

my_string = 'abcd'
print('%{}'.format(list(my_string)))

my_sentence = 'abracadabra, dreimal schwarzer kater'
print('%{}'.format(re.findall(r'\w+',my_sentence)))
print('%{}'.format(my_sentence.split()))

with open('tmpfile','w') as stream:
  for num in [1,15,100]:
    stream.write('{}\n'.format(num))

with open('tmpfile','r') as stream:
  for line in stream:
    print('%{}'.format(len(line)))

with open('tmpfile','r') as stream:
  my_sum = None
  for num in stream:
    num = num.rstrip()
    if my_sum is None:
       my_sum = num
    else:
      my_sum += num
  print('%my_sum={}'.format(my_sum))

seq = str()
with open('tmpfile','r') as stream:
  for line in stream:
    seq += line

lines = list()
with open('tmpfile','r') as stream:
  for line in stream:
    lines.append(line)
seq = ''.join(lines)

this_string = 'abcd'
for i in range(len(this_string)):
  print('%{} is suffix'.format(this_string[i:]))
  print('%{} is prefix'.format(this_string[:i+1]))

print('%{}'.format(this_string[-1]))

print('%{}'.format(this_string[::-1]))

f = 0.6
print('%f=',f)
print('%f={}'.format(f))

im_re = '(-?\s*\d+)\s*i'
for cs in ['7i-2','4-3i','9 i','-2',\
           '21-14i','-17 i+1']:
  m = re.search(r'{}'.format(im_re),cs)
  if not m:
    b = 0
    a = int(cs)
  else:
    b = int(m.group(1))
    if b < 0:
      b = '({})'.format(b)
    rest = re.sub(r'{}'.format(im_re),'',cs)
    if rest == '':
      a = 0
    else:
      a = int(rest)
  print('%{:10s} {}+{}i'.format(cs,a,b))

result = eval('[1,2,3].append(4)')
print('%{}'.format(result))

'''
result = eval('[x,y,z].append(1)')  # variables x y z are not known
'''
result = eval('[x,y,z].append(4)',{'x' : 1, 'y' : 2, 'z' : 3})
print('%{}'.format(result))

rows = 10
columns = 10
max_value = 9
index_sample \
  = set(random.sample([(i,j) for i in range(rows) for j in range(columns)],15))
value_list = [(i,j,random.randint(1,max_value)) for i,j in index_sample]
print('%{}'.format(value_list))
sparse_matrix = dict()
for i,j,v in value_list:
  sparse_matrix[(i,j)] = v
for i in range(rows):
  line = list()
  for j in range(rows):
    if (i,j) in sparse_matrix:
      line.append(sparse_matrix[(i,j)])
    else:
      line.append(0)
  print('%{}\\\\\\n'.format('&'.join(map(str,line))))

print('''\\documentclass[english]{beamer}
\\usepackage[english]{babel}
\\newcommand{\\InCcontext}{false}
\\usepackage{LocalDefs}
\\usepackage{LocalLST}

\\lstloadlanguages{Python}
\\lstset{language=Python}

\\title{Notions in Python Scripts}
\\begin{document}
\\begin{frame}[fragile,allowframebreaks]{Deciphering code fragments}''')

with open(__file__) as stream:
  for line in stream:
    m = re.search(r'#lst\{(\S+)\}',line)
    if m:
      print('\n\\Lstuse{{{}}}'.format(m.group(1)))

print('%./notions.py: [Errno 2] No such file or directory: \'xx\'')

print('''
%Traceback (most recent call last):
  %File "./notions.py", line 61, in <module>
    %with open('xx') as stream:
%FileNotFoundError: [Errno 2] No such file or directory: 'xx'
''')

print('''%differences between re.search, re.sub, s.translate''')

print('''%difference between / and //''')

print('''%https://stackoverflow.com/questions/16147344/is-list-join-really-faster-than-string-concatenation-in-python''')

print('''%interpret regular expression (-?\s*\d+)\s*i''')

print('''%debugging''')

print('''%matrix as list of lists, sparse matrix als dictionary''')

print('''
%[(9, 0, 3), (1, 3, 4), (9, 1, 2), (4, 8, 8), (3, 0, 5), (8, 1, 1), (5, 6, 7), (5, 8, 9), (3, 9, 4), (5, 0, 7), (7, 2, 4), (9, 6, 7), (2, 4, 7), (6, 5, 6), (9, 7, 1)]
%0&0&0&0&0&0&0&0&0&0\\
%0&0&0&4&0&0&0&0&0&0\\
%0&0&0&0&7&0&0&0&0&0\\
%5&0&0&0&0&0&0&0&0&4\\
%0&0&0&0&0&0&0&0&8&0\\
%7&0&0&0&0&0&7&0&9&0\\
%0&0&0&0&0&6&0&0&0&0\\
%0&0&4&0&0&0&0&0&0&0\\
%0&1&0&0&0&0&0&0&0&0\\
%3&2&0&0&0&0&7&1&0&0
''')

print('''
\\end{frame}
\\end{document}''')
