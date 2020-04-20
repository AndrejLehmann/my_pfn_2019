import sys

class Atom:
    def __init__(self,ident,name,x,y,z,atomtype,optional_list):
     # TODO
       return
    def __str__(self):
     # TODO
       return ''
    def __sub__(self,other):  # required only for LJ-Potential
      # TODO
      return

class Bond:
    def __init__(self,ident,atomid1,atomid2,kind,optional_list):
     # TODO
       return
    def atomid1(self):
      return self._atomid1
    def atomid2(self):
      return self._atomid2
    def __str__(self):
     # TODO
       return ''

class Molecule:
    def __init__(self,molecule_name,atom_list,bond_list):
     # TODO
       return
    def name(self):
     # TODO
       return ''
    def atoms_number(self):
     # TODO
       return -1
    def atom_list(self):
     # TODO
       return
    def bonds_number(self):
     # TODO
       return -1
    def __str__(self):
     # TODO
       return ''
    def __sub__(self,other):  # required only for LJ-Potential
      # TODO
      return
    def adjacency_matrix(self): # needed for shortest path algorithm
      # TODO
      return
