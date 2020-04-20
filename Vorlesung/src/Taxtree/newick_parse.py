#!/usr/bin/env python3

import argparse, re, sys
from operator import itemgetter
from taxtree import Taxtree

def showtaxonpath(lca,p0,p1,showpath):
  print('{}\t'.format(lca),end='')
  if showpath:
    print(','.join(p0) + '\t' + ','.join(p1))
  else:
    print('{}\t{}'.format(len(p0),len(p1)))

def check_args_consistency(args):
  if not args.lca:
    if args.path:
      sys.stderr.write('{}: option --path requires option --lca\n'
                       .format(sys.argv[0]))
      exit(1)
    if args.path_length:
      sys.stderr.write('{}: option --path_length requires option --lca\n'
                         .format(sys.argv[0]))
      exit(1)
  if args.subtree and args.statistics:
    sys.stderr.write(('{}: error: -s/--subtree: not allowed with argument '
                      '-c/--statistics\n').format(sys.argv[0]))
    exit(1)

def parse_arguments():
  p = argparse.ArgumentParser()
  og = p.add_mutually_exclusive_group(required=False)
  og.add_argument('-n','--newick_out',action='store_true',default=False,
                  help='output tree in newick format')
  og.add_argument('-x','--xml_out',action='store_true',default=False,
                  help='output tree in XML format')
  og.add_argument('-t','--tikz_out',action='store_true',default=False,
                  help=('output tree in tik format '
                        '(should only be used for small subtrees'))
  og.add_argument('-y','--node_out',action='store_true',default=False,
                  help='output tree in Node format')
  og.add_argument('-c','--statistics',action='store_true',default=False,
                  help=('output statistics (i.e.\ counts of different items) '
                        ' of tree'))
  p.add_argument('-s','--subtree',type=str,default=None,metavar='<taxon>',
                  help='output subtree of given taxon')
  p.add_argument('-i','--ignore',type=str,default=None,metavar='<regexp>',
                  help='ignore taxa matching the given regexp')
  p.add_argument('-f','--find',nargs='+',default=None,metavar='<taxon>',
                  help='find taxonomic identifiers in given file')
  p.add_argument('-a','--all_of_depth',type=int,default=None,metavar='<depth>',
                  help='output all taxonomic identifiers of given depth')
  p.add_argument('--sample',type=int,default=None,metavar='<size>',
                  help='output a sample of taxa of given size')
  p.add_argument('-l','--lca',type=str,default=None,metavar='<filename>',
                  help=('compute lowest common ancestors '
                        'for pairs of taxonomic units specified '
                        'in the given file with two taxa per line '
                        'and separated by a tabulator. The output '
                        'goes to STDOUT. In each line, the third '
                        'column containing the LCA of the two '
                        'taxa is added'))
  pg = p.add_mutually_exclusive_group(required=False)
  pg.add_argument('-p','--path',action='store_true',default=False,
                  help=('output paths from taxa to LCA '
                        '(when option --lca is used). The paths '
                        'for the first and second taxon is shown '
                        'comma-separated in column 4 and 5'))
  pg.add_argument('--path_length',action='store_true',default=False,
                  help=('output length of paths from taxa to LCA '
                        '(when option --lca is used). The length '
                        'of the paths are shown in column 4 and 5'))
  p.add_argument('inputfile',type=str,default=None,metavar='<inputfile>',
                  help=('read newick tree from given file'))
  args = p.parse_args()
  check_args_consistency(args)
  return args

args = parse_arguments()
taxtree = Taxtree(args.inputfile)
if args.statistics:
  depth, numbranching, numleaves, \
    branch_depth_dist, leaves_depth_dist = taxtree.statistics()
  print('{} contains tree of depth {} with {} branching nodes and {} leaves'
          .format(args.inputfile,depth,numbranching,numleaves))
  max_depth = max(max(leaves_depth_dist.keys()),max(branch_depth_dist.keys()))
  print('%Fields: depth, leaves_of_depth, branchnodes_of_depth')
  for d in range(max_depth+1):
    if d in leaves_depth_dist:
      ld = leaves_depth_dist[d]
    else:
      ld = 0
    if d in branch_depth_dist:
      bd = branch_depth_dist[d]
    else:
      bd = 0
    print('{}\t{}\t{}'.format(d,ld,bd))
  subtree_size = taxtree.subtree_sizes()
  subtree_height = taxtree.subtree_height()
  exceptlist = '^unclassified|^uncultured_bacteria'
  for name, size in sorted(subtree_size.items()):
    depth = taxtree.find_depth(name)
    if size >= 10 and size <= 20 and depth <= 3 and \
       not re.search(r'{}'.format(exceptlist),name):
      print('{} of depth {} has size {}'.format(name,depth,size))
  for name, height in sorted(subtree_height.items(),key=lambda k: k[1],\
                             reverse=True):
    if height < 8:
      break
    print('***{} of height {} and size {}'
           .format(name,height,subtree_size[name]))

if not args.subtree:
  if args.newick_out:
    taxtree.to_newick()
  if args.xml_out:
    taxtree.to_xml(sys.stdout)
  if args.node_out:
    taxtree.to_node_out(sys.stdout,0,taxtree.root())
    print('')
  if args.tikz_out:
    taxtree.to_tikz(sys.stdout,0,taxtree.root())
else:
  smallsubtreenode = taxtree.find_node(args.subtree)
  depth = taxtree.find_depth(args.subtree)
  assert smallsubtreenode
  if args.newick_out:
    taxtree.to_newick_rec(sys.stdout,0,smallsubtreenode,False)
  if args.xml_out:
    taxtree.to_xml_rec(sys.stdout,depth,smallsubtreenode)
  if args.tikz_out:
    taxtree.to_tikz(sys.stdout,depth,smallsubtreenode)
  if args.node_out:
    taxtree.to_node_out(sys.stdout,depth,smallsubtreenode)
    print('')

if args.lca:
  try:
    stream = open(args.lca)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  ln  = 0
  for line in stream:
    ln += 1
    taxons = line.rstrip().split('\t')
    if len(taxons) < 2:
      sys.stderr.write(('{}: file {}, line {} does not contain '
                        'two tab separated taxa')
                         .format(sys.argv[0],args.lca,ln))
      exit(1)
    print('{}\t{}\t'.format(taxons[0],taxons[1]),end='')
    if not taxtree.is_valid_id(taxons[0]) or not taxtree.is_valid_id(taxons[1]):
      result = '?'
      if args.path or args.path_length:
        result += '\t?\t?'
      print(result)
      continue
    if not args.path and not args.path_length:
      lca = taxtree.find_lca(taxons[0],taxons[1])
      print('{}'.format(lca))
    else: # output of path or path_length not shown here
      p0, p1 = taxtree.find_lca_paths(taxons[0],taxons[1])
      if len(p0) == 0:
        if len(p1) == 0:
          assert taxons[0] == taxons[1]
          lca = taxons[0]
        else:
          lca = p1[0]
      else:
        if len(p1) == 0:
          lca = p0[0]
        else:
          p00 = p0.pop(0)
          p10 = p1.pop(0)
          assert p00 == p10
          lca = p00
      showtaxonpath(lca,p0,p1,args.path)

if args.find:
  nameset = set()
  for filename in args.find.split(','):
    found = 0
    missing = 0
    try:
      stream = open(filename)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    for name in stream:
      if not args.ignore or not re.search(r'{}'.format(args.ignore),name):
        fname = name.rstrip()
        m = re.search(r'\s\(strain (.*)\)$',name)
        if m:
          fname = re.sub(r'\s\(strain .*\)$','',fname)
          strain_list = m.group(1).split('\/')
          strain_list = map(lambda s: re.sub(r'^\s+|\s+$','',s),strain_list)
          for strain in strain_list:
            if strain and not re.search(r'^\s*$',strain):
              nameset.add(re.sub(r'\s','_','{}_{}'.format(fname,strain)))
        else:
          fname = re.sub(r'\s','_',fname)
          nameset.add(fname)
    print('process {}'.format(filename))
    for name in sorted(nameset):
      if taxtree.search_node(name):
        found += 1
      else:
        witness = taxtree.search_name_lcp(name)
        print('cannot find '{}', closest={}'.format(name,witness))
        missing += 1
    print('{} found = {}'.format(filename,found))
    print('{} missing = {}'.format(filename,missing))
    nameset.clear()

if args.all_of_depth:
  for name in taxtree.enum_nodes_of_depth(args.all_of_depth):
    print(name)

if args.sample:
  odd = False
  for name in taxtree.sample_names(args.sample):
    print(name,end='')
    if odd:
      print('')
      odd = False
    else:
      print('\t',end='')
      odd = True

# print(taxtree.find_path('Brasilonema_bromeliae'))
