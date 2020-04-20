import re
def parse_features(features):
  for m in re.finditer('^ {5}\S.*\n( {21}\S.*\n)*',\
                       features, flags = re.M):
    yield m.group(0)
