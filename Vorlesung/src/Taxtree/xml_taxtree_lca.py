#!/usr/bin/env python3

import sys, argparse

def enum_path2leaves(xml_tree_root):
  path = list()
  stack = list()
  stack.append((0,xml_tree_root))
  while stack:
    level, node = stack.pop()
    assert node.text
    if level >= len(path):
      assert len(path) == level
      path.append((node.tag,node.text.strip()))
    else:
      path[level] = (node.tag,node.text.strip())
    children_of_node = list()
    # first collect all children and then push them in reversed
    # order so that the first child is processed before the second children
    # etc
    for child in node:
      children_of_node.append((level+1,child))
    if children_of_node:
      for elem in reversed(children_of_node):
        stack.append(elem)
    else:
      yield path, level+1

def node2path_map_get(xml_tree_root):
  node2path_map = dict()
  for path, path_length in enum_path2leaves(xml_tree_root):
    assert path
    for idx in range(path_length):
      end_node = path[idx][1]
      if not (end_node in node2path_map):
        new_path = [path[j][1] for j in range(idx+1)]
        node2path_map[end_node] = new_path
  return node2path_map

import xml.etree.ElementTree as ET

class TaxtreeXML:
  def __init__(self,xmlfilename):
    try:
      xml_tree = ET.parse(xmlfilename)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    self._xml_tree_root = xml_tree.getroot()
    self._parent_map = dict()
    root_name = self._xml_tree_root.text.strip()
    self._parent_map[root_name] = None
    stack = [self._xml_tree_root]
    self._node2path_map = node2path_map_get(self._xml_tree_root)
    while stack:
      node = stack.pop()
      assert node.text
      node_text = node.text.strip()
      for child in node:
        stack.append(child)
        self._parent_map[child.text.strip()] = node_text
  def find_path(self,name):
    path = list()
    while name:
      path.append(name)
      name = self._parent_map[name]
    return list(reversed(path))
  def find_lca(self,name1,name2):
    path1 = self.find_path(name1)
    path2 = self.find_path(name2)
    for idx in range(0,min(len(path1),len(path2))):
      if path1[idx] != path2[idx]:
        assert idx > 0
        return path1[idx-1]
    assert min(len(path1),len(path2)) > 0
    return path1[min(len(path1),len(path2))-1]
  def find_lca2(self,name1,name2):
    assert name1 in self._node2path_map
    assert name2 in self._node2path_map
    path1 = self._node2path_map[name1]
    path2 = self._node2path_map[name2]
    for idx in range(0,min(len(path1),len(path2))):
      if path1[idx] != path2[idx]:
        assert idx > 0
        return path1[idx-1]
    assert min(len(path1),len(path2)) > 0
    return path1[min(len(path1),len(path2))-1]

def parse_arguments():
  p = argparse.ArgumentParser()
  p.add_argument('taxonpairs',type=str,
                  help='specify input files with pairs of taxon, tab sep')
  p.add_argument('taxtree',type=str,
                  help='specify input files with taxonomic tree')
  return p.parse_args()

args = parse_arguments()
taxtree = TaxtreeXML(args.taxtree)
try:
  stream = open(args.taxonpairs)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)
for linenum, line in enumerate(stream):
  taxons = line.rstrip().split('\t')
  if len(taxons) < 2:
    sys.stderr.write(('{}: file {}, line {} does not contain '
                      'two tab separated taxa')
                       .format(sys.argv[0],args.lca,linenumn))
    exit(1)
  lca = taxtree.find_lca(taxons[0],taxons[1])
  lca2 = taxtree.find_lca2(taxons[0],taxons[1])
  assert lca == lca2
  print('{}\t{}\t{}'.format(taxons[0],taxons[1],lca))
