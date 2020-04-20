#!/usr/bin/env python3

import xml.etree.ElementTree as ET

# show subtags with text/name
def xmlshownextlevel(idset,node):
  for child in node:
    if child.tag in idset:
      print('{} = {}'
            .format(child.tag,
                    child.text))

# specify which tags produce output

idset = ['Seq_locus', 'Seq_sequence',
          'Seq_division']
xml_tree = ET.parse('Record.xml')
root = xml_tree.getroot()
print('# process {}'.format(root.tag))
xmlshownextlevel(idset,root)
