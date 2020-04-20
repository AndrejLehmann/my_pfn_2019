#!/usr/bin/env python3

import sys, xml.sax
from generic_xml_handler import GenericXMLHandler

def proc_end(thisdict,proc_info):
  taglist = ['query','name','score']
  line_values = list()
  for showtag in taglist:
    assert showtag in thisdict
    line_values.append(thisdict[showtag])
  print('\t'.join(line_values))

# create an XMLReader
xmlparser = xml.sax.make_parser()
# turn off namepsaces
xmlparser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
handler = GenericXMLHandler('hit',proc_end,None)
xmlparser.setContentHandler(handler)
xmlparser.parse('swipe-output.xml')
