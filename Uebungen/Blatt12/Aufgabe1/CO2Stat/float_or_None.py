def float_or_None(v):
  if len(v) == 0:
    return None
  try:
    f = float(v)
  except ValueError:
    return None
  return f
