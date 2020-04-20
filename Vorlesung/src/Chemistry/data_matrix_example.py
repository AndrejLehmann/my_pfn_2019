#!/usr/bin/env python3

from data_matrix import *

lines = ['atomicNumber	symbol	name	meltingPoint',
         '1	H	Hydrogen	14',
         '2	He	Helium	',
         '3	Li	Lithium	454']

attribute_list, atom_matrix = data_matrix_new(lines)
my_attributes = ['name','meltingPoint']
my_elements = ['H','Li']
data_matrix_show(atom_matrix,' ',my_attributes,my_elements)
