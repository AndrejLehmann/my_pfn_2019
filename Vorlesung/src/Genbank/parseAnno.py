import re
from collections import OrderedDict
def parse_annotation(annotation):
  results = OrderedDict() # entries are ordered by time of input

  # mark beginnings with special character and split there
  sep = '\001'   # \1 is back reference to first group
  tops = re.sub('\n([A-Z])', '\n{}\\1'.format(sep),\
                annotation).split(sep)
  for value in tops:
    # get key from line, mo is match object
    # the BASE COUNT has a space in it, treat separately
    mo = re.search(r'^(BASE COUNT|[A-Z]+)',value)
    if mo:
      key = mo.group(1)
    else:
      sys.stderr.write('{}: Cannot find key in line {}\n'
                        .format(sys.argv[0],value))
      exit(1)
    results[key] = value   # store value in the dictionary
  return results
