#!/usr/bin/env python3

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
  def __init__(self):
    self.current_data = None
    self.current_type = None
    self.current_format = None
    self.year = None
    self.rating = None
    self.stars = None
    self.description = None

  # Call when an element starts
  def startElement(self, tag, attributes):
    self.current_data = tag
    if tag == 'movie':
      print('*****movie*****')
      title = attributes['title']
      print('title: {}'.format(title))

  # Call when an elements ends
  def endElement(self, tag):
    if self.current_data == 'type':
      print('type: {}'.format(self.current_type))
    elif self.current_data == 'format':
      print('format: {}'.format(self.current_format))
    elif self.current_data == 'year':
      print('year: {}'.format(self.year))
    elif self.current_data == 'rating':
      print('rating: {}'.format(self.rating))
    elif self.current_data == 'stars':
      print('stars: {}'.format(self.stars))
    elif self.current_data == 'description':
      print('description: {}'.format(self.description))
    self.current_data = None

  # Call when a character is read
  def characters(self, content):
    if self.current_data == 'type':
      self.current_type = content
    elif self.current_data == 'format':
      self.current_format = content
    elif self.current_data == 'year':
      self.year = content
    elif self.current_data == 'rating':
      self.rating = content
    elif self.current_data == 'stars':
      self.stars = content
    elif self.current_data == 'description':
      self.description = content

if  __name__ == '__main__':
  # create an XMLReader
  parser = xml.sax.make_parser()
  # turn off namepsaces
  parser.setFeature(xml.sax.handler.feature_namespaces, 0)

  # override the default ContextHandler
  Handler = MovieHandler()
  parser.setContentHandler( Handler )

  parser.parse('movies.xml')
