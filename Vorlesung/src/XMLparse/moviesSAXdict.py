#!/usr/bin/env python3

import xml.sax
from generic_xml_handler import GenericXMLHandler

SHOWTAG_LIST = ['title','type','format','year','rating','stars',
                'description']

def proc_end(thisdict,proc_info):
  print('*****movie*****')
  for showtag in SHOWTAG_LIST:
    if showtag in thisdict:
      print('{}: {}'.format(showtag,thisdict[showtag]))

# create an XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# override the default ContextHandler
handler = GenericXMLHandler('movie',proc_end,None)
parser.setContentHandler(handler)
parser.parse('movies.xml')
