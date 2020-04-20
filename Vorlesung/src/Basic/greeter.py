#!/usr/bin/env python3

class Greeter:
  def initialize(name = 'World'):
    self.name = name
  def say_hi(self):
    print('Hi {}!'.format(self.name))
  def say_bye(self):
    print('Bye {}, come back soon.'.format(self.name))
