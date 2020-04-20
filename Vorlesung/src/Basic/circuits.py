#!/usr/bin/env python3
class LogicGate:
  def __init__(self,n):
    self.label = n
    self.output = None

  def getLabel(self):
    return self.label

  def getOutput(self):
    self.output = self.performGateLogic()
    return self.output

class BinaryGate(LogicGate):
  def __init__(self,n):
    LogicGate.__init__(self,n)
    self.pinA = None
    self.pinB = None

  def getPinA(self):
    text = 'Enter Pin A input for gate '
    return int(input(text + self.getLabel()+'-->'))

  def getPinB(self):
    text = 'Enter Pin B input for gate '
    return int(input(text + self.getLabel()+'-->'))

class UnaryGate(LogicGate):
  def __init__(self,n):
    LogicGate.__init__(self,n)
    self.pin = None

  def getPin(self):
    text = 'Enter Pin input for gate '
    return int(input(text + self.getLabel()+'-->'))

class AndGate(BinaryGate):
  def __init__(self,n):
    BinaryGate.__init__(self,n)

  def performGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()
    if a == 1 and b == 1:
      return 1
    else:
      return 0
