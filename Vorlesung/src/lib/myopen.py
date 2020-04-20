import sys
def myopen(filename,mode='r'):
  try:
    stream = open(filename,mode)
  except IOError as err:
    sys.stderr.write('{}: {}\n',sys.argv[0],err)
    exit(1)
  return stream
