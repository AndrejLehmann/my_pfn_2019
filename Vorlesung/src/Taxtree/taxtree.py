#!/usr/bin/env python3

import re, sys, random
from collections import defaultdict
from lexical_units import LexicalKind, lexical_units_enum

class Node:
  def __init__(self,name,successors):
    self.name = name
    self.successors = successors

class Edge:
  def __init__(self,parent,node,depth,visited):
    self.parent = parent
    self.node = node
    self.depth = depth
    self.visited = visited

class Taxtree:
  def __init__(self,inputfile):
    self._root = None   # instance var to hold root of tax. tree
    stack = list()
    for lex_unit in lexical_units_enum(inputfile):
      if lex_unit[0] == LexicalKind.OPEN: # new node no name yet
        newbranch = Node(None,list())
        stack.append(newbranch) # stack top contains current node
      elif lex_unit[0] == LexicalKind.CLOSE: # complete branch node
        assert stack  # stack must contain at least one br.node
        brnode = stack.pop()
        brnode.name = lex_unit[1] # store name of br. node
        if not stack:  # if stack is empty
          self._root = brnode   # now tree is complete
        else: # parent of brnode is top element of stack
          stack[-1].successors.append(brnode)
      else: # lexical unit is LEAF
        assert lex_unit[0] == LexicalKind.LEAF and stack
        # leaf with empy list of successors
        newleaf = Node(lex_unit[1],list())
        # parent of leaf is top element of stack
        stack[-1].successors.append(newleaf)
    assert not stack and self._root is not None
    self._name_map = dict()
    for node, depth, parent in self.enum_nodes():
      assert node.name not in self._name_map
      self._name_map[node.name] = (node, depth, parent)
  def root(self):
    return self._root

  def to_newick_rec(self,fo,depth,node,last_successor):
    indentation = ' ' * (2 * depth)
    fo.write(indentation + '(\n')  # start of subtree for br. node
    lastidx = len(node.successors) - 1 # output successor subtrees
    for idx, subnode in enumerate(node.successors):
      if not subnode.successors:  # subnode is leaf
        termsymbol = '' if idx == lastidx else ','
        fo.write(indentation + '  {}{}\n'
                  .format(subnode.name,termsymbol))
      else:
        self.to_newick_rec(fo,depth+1,subnode,idx == lastidx)
    if last_successor:  # is node last successor of parent?
      termsymbol = ''
    else:
      termsymbol = ',' if depth > 0 else ';'
    # now output name of branching node
    fo.write(indentation + '){}{}\n'.format(node.name,termsymbol))

  def to_newick(self,fo = sys.stdout):
    self.to_newick_rec(fo,0,self._root,False)
  def to_node_out(self,fo,depth,node):
    indentation = ' ' * (2 * depth)
    fo.write('Node("{}",'.format(node.name))
    if not node.successors:
      fo.write('[])')
    else:
      fo.write('[')
      numsucc = len(node.successors)
      for idx, subnode in enumerate(node.successors):
        self.to_node_out(fo,depth+1,subnode)
        if idx < numsucc - 1:
          fo.write(',')
      fo.write('])')
  def to_tikz(self,fo,depth,node):
    indentation = ' ' * (2 * depth)
    fo.write(indentation + '[{}'.format(self.latexshow(node.name)))
    if not node.successors:
      fo.write(']\n')
    else:
      fo.write('\n')
      for subnode in node.successors:
        self.to_tikz(fo,depth+1,subnode)
      fo.write(indentation + ']\n')

  def find_node(self,name):
    assert name in self._name_map
    node, depth, parent = self._name_map[name]
    return node

  def find_depth(self,name):
    assert name in self._name_map
    node, depth, parent = self._name_map[name]
    return depth

  def find_parent(self,name):
    assert name in self._name_map
    node, depth, parent = self._name_map[name]
    return parent

  def is_valid_id(self,name):
    return name in self._name_map

  def search_node(self,name):
    if name in self._name_map:
      node, depth, parent = self._name_map[name]
      return node
    else:
      return None

  def enum_nodes_of_depth(self,selectdepth):
    for node, depth, parent in self.enum_nodes():
      if depth == selectdepth:
        yield node.name

  def statistics(self):
    maxdepth, numleaves, numbranching = 0, 0, 0
    leaves_depth_dist = defaultdict(int)
    branch_depth_dist = defaultdict(int)
    for node, depth, parent in self.enum_nodes():
      if maxdepth < depth:
        maxdepth = depth
      if not node.successors:
        numleaves += 1
        leaves_depth_dist[depth] += 1
      else:
        numbranching += 1
        branch_depth_dist[depth] += 1
    return maxdepth, numbranching, numleaves, \
           branch_depth_dist, leaves_depth_dist

  def subtree_sizes(self):
    subtree_size = defaultdict(int)
    stack = list()
    stack.append(Edge(None,self._root,0,False))
    while stack:
      elem = stack[-1]
      if not elem.visited:
        elem.visited = True
        for subnode in elem.node.successors:
          if not subnode.successors:
            subtree_size[elem.node.name] += 1
          else:
            stack.append(Edge(elem.node,subnode,
                              elem.depth+1,False))
      else:
        if elem.parent:
          subtree_size[elem.parent.name] += subtree_size[elem.node.name]
        stack.pop()
    return subtree_size

  def subtree_height(self):
    subtree_height = defaultdict(int)
    stack = list()
    stack.append(Edge(None,self._root,0,False))
    while stack:
      elem = stack[-1]
      if not elem.visited:
        elem.visited = True
        for subnode in elem.node.successors:
          if not subnode.successors:
            subtree_height[elem.node.name] = 0
          else:
            stack.append(Edge(elem.node,subnode,
                              elem.depth+1,False))
      else:
        if elem.parent:
          if subtree_height[elem.parent.name] < \
                subtree_height[elem.node.name] + 1:
            subtree_height[elem.parent.name] = subtree_height[elem.node.name]+1
        stack.pop()
    return subtree_height
  def find_path(self,name):
    path = list()
    node = self.find_node(name)
    while node:
      path.append(node.name)
      node = self.find_parent(node.name)
    return list(reversed(path))

#BEGIN{exclude}
  def find_lca(self,name1,name2):
    path1 = self.find_path(name1)
    path2 = self.find_path(name2)
    for idx in range(0,min(len(path1),len(path2))):
      if path1[idx] != path2[idx]:
        assert idx > 0
        return path1[idx-1]
    assert min(len(path1),len(path2)) > 0
    return path1[min(len(path1),len(path2))-1]

  def find_lca_paths(self,name1,name2):
    path1 = self.find_path(name1)
    path2 = self.find_path(name2)
    #print('path1={}'.format(path1))
    #print('path2={}'.format(path2))
    lcp = 0
    for idx in range(0,min(len(path1),len(path2))):
      assert lcp == idx
      if path1[lcp] != path2[lcp]:
        break
      lcp += 1
    if lcp == 0:
      return list(),list()
    return path1[lcp-1:], path2[lcp-1:]

  def sample_names(self,num):
    return random.sample(self._name_map.keys(),num)
#END{exclude}

  taxonomic_rank = ['domain', 'superkingdom', 'phylum',
                    'subphylum', 'class', 'subclass', 'order',
                    'suborder', 'family', 'subfamiliy', 'tribe',
                    'genus', 'subgenus', 'species', 'subspecies']

  def to_xml_rec(self,fo,depth,node):
    indentation = ' ' * (2 * depth)
    rank = self.taxonomic_rank[depth + 1]
    fo.write(indentation +
             '<{}> {}'.format(rank,self.xmlshow(node.name)))
    if not node.successors:
      fo.write(' </{}>\n'.format(rank))
    else:
      fo.write('\n')
      for subnode in node.successors:
        self.to_xml_rec(fo,depth+1,subnode)
      fo.write(indentation + '</{}>\n'.format(rank))

  def to_xml(self,fo,depth = 0):
    self.to_xml_rec(fo,depth,self._root)
  def enum_nodes(self):  # depth first enumeration
    stack = list()
    stack.append((self._root,0))
    yield self._root, 0, None  # root.parent is None
    while stack:
      branchnode, depth = stack.pop()
      for subnode in branchnode.successors:
        if subnode.successors:  # a branching node?
          stack.append((subnode,depth+1))
        yield subnode, depth+1, branchnode

  def search_name_lcp(self,name):
    if self._name_list is None:
      self._name_list = sorted(self._name_map.keys())
    witness = binarysearch(0,len(self._list) - 1,name)
    return witness

  # now declare private methods

  def _mystrcmp(s,t):
    for idx in range(0,min(len(s),len(t))):
      a = str.upper(s[idx])
      b = str.upper(t[idx])
      if a < b:
        return idx, -1
      elif a > b:
        return idx, +1
    if len(s) < len(t):
      return s.length, -1
    elif len(s) > len(t):
      return len(t), +1
    else:
      return len(t), 0

  def binarysearch(self,left,right,name):
    lcpmax = None
    witness = None
    iteration = 0
    while left <= right:
      mid = left + (right - left)/2
      lcp, cmp_value = self._mystrcmp(name,self.name[mid])
      if lcpmax is None or lcpmax < lcp:
        lcpmax = lcp
        witness = self.name[mid]
      if cmp_value < 0:
        right = mid - 1
      elif cmp_value > 0:
        left = mid + 1
      else:
        break
      iteration += 1
    assert witness is not None
    return witness

  def latexshow(self,s):
    sl = list()
    for cc in s:
      if cc == '_':
        sl.append('\\_')
      else:
        sl.append('{}'.format(cc))
    return ''.join(sl)

  def xmlshow(self,s):
    badchar = '><&'
    if re.search(r'[{}]'.format(badchar),s):
      sl = list()
      for cc in s:
        if cc != '.' and (cc in badchar):
          sl.append('<![CDATA[{}]]>'.format(cc))
        else:
          sl.append('{}'.format(cc))
      return ''.format(sl)
    else:
      return s
# end of class

'''
Clostridium_sp._AB<![CDATA[&]]>J
'''
