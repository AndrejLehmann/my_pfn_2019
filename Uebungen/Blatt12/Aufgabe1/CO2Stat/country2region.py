import sys

class Country2Region:
  def __init__(self):
    try:
      stream = open('country2region.tsv')
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    self._cc_map = dict()
    self._cr_map = dict()
    for linenum, line in enumerate(stream,1):
      values = line.strip().split('\t')
      assert len(values) >= 2, "for {}".format(values)
      country = values[0]
      assert not country in self._cc_map
      self._cc_map[country] = values[1]
      if len(values) >= 3:
        assert not country in self._cr_map
        self._cr_map[country] = values[2]
  def continents(self):
    return set(sorted(self._cc_map.values()))
  def regions(self):
    return set(sorted(self._cr_map.values()))
  def continent(self,country):
    if not country in self._cc_map:
      sys.stderr.write('{}: continent for {} not defined\n'
                        .format(sys.argv[0],country))
      exit(1)
    return self._cc_map[country]
  def region(self,country):
    if not country in self._cr_map:
      return None
    return self._cr_map[country]
