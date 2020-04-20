from color_map import COLOR_MAP
class PriorityQueue:
  def __init__(self):
    self._dict = dict()

  def is_empty(self):
    return len(self._dict) == 0

  def __contains__(self, key):  # overload in operator
    return key in self._dict

  def set_priority(self, key, priority):
    self._dict[key] = priority

  def extract_min(self):
    prio_max, key_max = None, None
    for key, value in self._dict.items():
      if prio_max is None or value < prio_max:
        key_max, prio_max = key, value
    assert key_max is not None
    del self._dict[key_max]
    return key_max

  def __iter__(self):
    return iter(sorted(self._dict.items(), key=lambda x: x[1]))

  def __str__(self):
    return ', '.join(['\\textcolor{{{}}}{{{}}}({})'
                      .format(COLOR_MAP[hash(key)], hash(key), value) \
                                for key, value in self])
