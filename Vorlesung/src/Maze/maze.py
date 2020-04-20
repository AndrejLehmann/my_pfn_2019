#!/usr/bin/env python3

import argparse, sys, re, random
from priority_queue import PriorityQueue
from enum import Enum

def rand_perm_fisher_yates(elems):
  num_elems = len(elems)
  for idx in range(num_elems,0,-1):
    r = random.randint(0,idx-1)
    assert r >= 0 and r < num_elems
    tmp = elems[idx-1]
    elems[idx-1] = elems[r]
    elems[r] = tmp
  return elems

def draw_grid(num_rows,num_cols):
  print('\\draw[step=1cm, gray, very thin] (0, 0) grid ({}, {});'
         .format(num_cols,num_rows))

def latex_header(noheader,origin,scale,num_rows,num_cols):
  if not noheader:
    print('''\\documentclass{beamer}
             \\usetheme{Boadilla}
             \\usepackage{tikz}
             \\begin{document}
             \\begin{frame}{}
             \\begin{center}''')
  print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
  draw_grid(num_rows,num_cols)
  if origin:
    print('\\node at (0,-0.7) {{$(0,0)$}};')

def latex_footer(noheader):
  print('\\end{tikzpicture}')
  if not noheader:
    print('''\\end{center}
             \\end{frame}
             \\end{document}''')

def make_dot(i,j,color):
  return '\\fill[{}] ({}, {}) circle (10pt);'.format(color,j+0.5,i+0.5)

def mark2string(sq,val):
  if val == 'EXPL':
    return make_dot(sq[0],sq[1],'red')
  if val == 'EXIT':
    return make_dot(sq[0],sq[1],'green')
  i, j = sq
  k, l = val
  return ('\\draw[green,->,-latex] ({},{}) -- ({},{});'
          .format(j+0.5,i+0.5,l+0.5,k+0.5))

EXPL = -2
EXIT = -1

class ActionKind(Enum):
  CALL_MARK_RETURN = 0
  CALL_CMP_RETURN = 1
  CALL_MARK = 2
  MARK_RETURN = 3
  RETURN = 4

class MazeAction:
  def __init__(self,sq,action,level,value,retval = None):
    self._sq = sq
    self._action = action
    self._level = level
    self._value = value
    self._retval = retval
  def mark(self):
    if self._action == ActionKind.CALL_MARK_RETURN or \
       self._action == ActionKind.CALL_MARK or \
       self._action == ActionKind.MARK_RETURN:
      assert not self._sq is None
      assert not self._value is None
      return self._sq, self._value
    else:
      return None

  def __str__(self):
    sep = '$\\Rightarrow$'
    if self._action == ActionKind.CALL_MARK_RETURN:
      s = ('call s\\_r({sq}) {sep} mark[{sq}]={val} {sep} return {retval}'
           .format(sq=self._sq,sep=sep,val=self._value,retval=self._retval))
    elif self._action == ActionKind.CALL_CMP_RETURN:
      s = ('call s\\_r({sq}) {sep} mark[{sq}]=={val} {sep} return {retval}'
           .format(sq=self._sq,sep=sep,val=self._value,retval=self._retval))
    elif self._action == ActionKind.CALL_MARK:
      s = ('call s\\_r({sq}) {sep} mark[{sq}]={val}'
           .format(sq=self._sq,sep=sep,val=self._value))
    elif self._action == ActionKind.MARK_RETURN:
      s = ('mark[{sq}]={val} {sep} return {retval}'
           .format(sq=self._sq,sep=sep,val=self._value,retval=self._retval))
    elif self._action == ActionKind.RETURN:
      s = ('return {retval}'
           .format(retval=self._retval))
    indent = '\\hspace*{{{}pt}}'.format(3 * self._level)
    return '{}{}'.format(indent,s)

def mark_history_get(actions):
  mark_history = dict()
  for idx, action in enumerate(actions):
    mark = action.mark()
    if not mark is None:
      sq, value = mark
      if not sq in mark_history:
        mark_history[sq] = list()
      mark_history[sq].append((idx,value))
  return mark_history

class Maze:
  infty = sys.maxsize
  def __init__(self,maze_rows):
    max_column = 0
    for rows in maze_rows.values():
      max_column = max(max_column,
                       max(rows))
    self._num_rows = len(maze_rows)
    self._num_cols = max_column + 1
    self._matrix = dict()
    self._rand_dir_ord = False
    for i in range(0,self._num_rows):
      self._matrix[i] = dict()
      for j in range(0,self._num_cols):
        if j in maze_rows[i]:
          self._matrix[i][j] = 1
        else:
          self._matrix[i][j] = 0
  def rand_dir_ord(self,value):
    self._rand_dir_ord = vale
  def start_color(self):
    return 'blue!50!white'
  def show_matrix_values(self):
    for i in range(0,self._num_rows):
      for j in range(0,self._num_cols):
        print('\\node at ({}, {}) {{{{\\scriptsize {}}}}};'
              .format(j+0.5,i+0.5,self._matrix[i][j]))
  def show_matrix_grayblocks(self):
    for i in range(0,self._num_rows):
      for j in range(0,self._num_cols):
        if self._matrix[i][j]:
          print('\\fill[black!50] ({}, {}) rectangle ({}, {});'
                 .format(j,i,j+1,i+1))
  def show_tikz(self,grayblocks,noheader,origin,scale,square_list = None):
    latex_header(noheader,origin,scale,self._num_rows,self._num_cols)
    if grayblocks:
      self.show_matrix_grayblocks()
      if square_list:
        assert len(square_list) > 0
        i, j = square_list[0]
        print(make_dot(i,j,self.start_color()))
        edge_squares = list()
        for square in square_list:
          i, j = square
          edge_squares.append((j+0.5,i+0.5))
        print('\\draw[blue, thick] {};'
               .format(' -- '.join(map(str,edge_squares))))
    else:
      self.show_matrix_values()
    latex_footer(noheader)
  def isexit(self,square):
    i, j = square
    if i == -1 or i == self._num_rows or \
       j == -1 or j == self._num_cols:
      return True
    return False
  def neighbors(self,square):
    i, j = square
    assert self._matrix[i][j] == 0
    neighbors_list = list()
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    if self._rand_dir_ord:
      rand_perm_fisher_yates(directions)
    for idiff, jdiff in directions:
      n_i = i + idiff
      n_j = j + jdiff
      if self.isexit((n_i,n_j)) or \
         (n_i >= 0 and n_i < self._num_rows and \
          n_j >= 0 and n_j < self._num_cols and \
          self._matrix[n_i][n_j] == 0):
        neighbors_list.append((n_i,n_j))
    return neighbors_list
  def open_squares(self):
    squares = list()
    for i in range(0,self._num_rows):
      for j in range(0,self._num_cols):
        if self._matrix[i][j] == 0:
          squares.append((i,j))
    return squares
  def paths2exit(self,startsquare):
    def paths2exit_rec(paths,square,this_path):
      i, j = square
      assert self._matrix[i][j] == 0
      this_path.append(square)
      for next_sq in self.neighbors(square):
        if self.isexit(next_sq):
          this_path.append(next_sq)
          paths.append(this_path)
        elif next_sq not in this_path:
          new_path = this_path.copy()
          paths2exit_rec(paths,next_sq,new_path)
    paths = list()
    paths2exit_rec(paths,startsquare,list())
    return paths
  def isborder(self,square):
    i, j = square
    if i == 0 or i == self._num_rows - 1 or \
       j == 0 or j == self._num_cols - 1:
      return True
    return False
  def shortest_path2exit2(self,startsquare):
    pq = PriorityQueue()
    distance = dict()
    pred = dict()
    on_border = set()
    for square in self.open_squares():
      pq.set_priority(square,Maze.infty)
      if self.isborder(square):
        on_border.add(square)
    pq.set_priority(startsquare,0)
    distance[startsquare] = 0
    while not pq.is_empty():
      square = pq.extract_min()
      if not square in distance:
        continue
      dsquare = distance[square] + 1
      for next_sq in self.neighbors(square):
        if next_sq in pq and \
           ((not next_sq in distance) or dsquare < distance[next_sq]):
          distance[next_sq] = dsquare
          pq.set_priority(next_sq,dsquare)
          pred[next_sq] = square
    min_dist = None
    min_b = None
    for b in on_border:
      if min_dist is None or min_dist > distance[b]:
        min_dist = distance[b]
        min_b = b
    b = min_b
    path = list()
    while b != startsquare:
      path.append(b)
      b = pred[b]
    path.append(startsquare)
    return min_dist, list(reversed(path))
  def shortest_path2exit3(self,startsquare):
    distance = dict()
    pred = dict()
    queue = [startsquare]
    distance[startsquare] = 0
    while queue:
      square = queue.pop(0)
      assert square in distance
      for next_sq in self.neighbors(square):
        if (not self.isexit(next_sq)) and (not next_sq in distance):
          distance[next_sq] = distance[square] + 1
          queue.append(next_sq)
          pred[next_sq] = square
    min_dist = None
    min_b = None
    for square in self.open_squares():
      if self.isborder(square) and \
         (min_dist is None or min_dist > distance[square]):
        min_dist = distance[square]
        min_b = square
    b = min_b
    path = list()
    while b != startsquare:
      path.append(b)
      b = pred[b]
    path.append(startsquare)
    return min_dist, list(reversed(path))
  def shortest_path2exit(self,startsquare):
    spath = [None,None] # len and path as list
    def shortest_path2exit_rec(square,curr_path):
      i, j = square
      assert self._matrix[i][j] == 0
      if spath[0] is None or\
         spath[0] > len(curr_path) + 1:
        curr_path.append(square)
        for next_sq in self.neighbors(square):
          if self.isexit(next_sq):
            curr_path.append(next_sq)
            if spath[0] is None or\
               spath[0] > len(curr_path):
              spath[0] = len(curr_path)
              spath[1] = curr_path
          elif next_sq not in curr_path:
            new_path = curr_path.copy()
            shortest_path2exit_rec(next_sq,new_path)
    shortest_path2exit_rec(startsquare,list())
    return spath[1]
  def shortest_path2exit_itrtv(self,
                               startsquare,df):
    spath_len, spath = None, None
    tasks = [(startsquare,list())]
    while tasks:
      pop_idx = (len(tasks)-1) if df else 0
      square, curr_path = tasks.pop(pop_idx)
      i, j = square
      assert self._matrix[i][j] == 0
      if spath_len is None or\
         spath_len > len(curr_path) + 1:
        curr_path.append(square)
        for next_sq in self.neighbors(square):
          if self.isexit(next_sq):
            curr_path.append(next_sq)
            if spath_len is None or\
               spath_len > len(curr_path):
              spath_len = len(curr_path)
              spath = curr_path
          elif next_sq not in curr_path:
            new_path = curr_path.copy()
            tasks.append((next_sq,new_path))
    return spath
  def collect_path(self,mark,startsquare):
    sq = startsquare
    path = [startsquare]
    while True:
      assert (sq in mark) and mark[sq] != EXPL
      next_sq = mark[sq]
      if next_sq == EXIT:
        break
      path.append(next_sq)
      sq = next_sq
    return path
  def somepath2exit(self,start):
    mark = dict()
    def somepath2exit_rec(sq):
      if self.isexit(sq):
        mark[sq] = EXIT
        return 0
      if sq in mark and mark[sq] == EXPL:
        return -1
      mark[sq] = EXPL
      path_len = -1
      for next_sq in self.neighbors(sq):
        path_len = somepath2exit_rec(next_sq)
        if path_len >= 0:
          mark[sq] = next_sq
          path_len += 1
          break
      return path_len
    path_len = somepath2exit_rec(start)
    if path_len < 0: return None
    return path_len, mark
  def somepath2exit_iter(self,startsquare,iterations):
    self._rand_dir_ord = True
    min_path_len, min_mark = None, None
    for _ in range(iterations):
      found = self.somepath2exit(startsquare)
      if found:
        path_len, mark = found
        if min_path_len is None or min_path_len > path_len:
          min_path_len = path_len
          min_mark = mark
    if min_mark:
      return maze.collect_path(min_mark,startsquare)
    return None
  def somepath2exit_iter_args(self,somepath_arg):
    mo = re.search(r'(.*)/(\d+)',somepath_arg)
    if not mo:
      sys.stderr.write('{}: cannot parse argument {}\n'.format(sys.argv[0],
                                                               args.somepath))
      exit(1)
    startsquare = eval(mo.group(1))
    iterations = int(mo.group(2))
    path = None
    if iterations == 0:
      found = self.somepath2exit(startsquare)
      if found is not None:
        path_len, mark = found
        path = self.collect_path(mark,startsquare)
    else:
      path = self.somepath2exit_iter(startsquare,iterations)
    return startsquare, path

  def somepath2exit_track(self,scale,startsquare):
    mark = dict()

    def somepath2exit_rec(lev,actions,sq):
      if self.isexit(sq):
        mark[sq] = EXIT
        actions.append(MazeAction(sq,ActionKind.CALL_MARK_RETURN,lev,'EXIT',0))
        return 0
      if (sq in mark) and mark[sq] == EXPL:
        actions.append(MazeAction(sq,ActionKind.CALL_CMP_RETURN,lev,'EXPL',-1))
        return -1
      mark[sq] = EXPL
      actions.append(MazeAction(sq,ActionKind.CALL_MARK,lev,'EXPL'))
      path_len = -1
      for next_sq in self.neighbors(sq):
        path_len = somepath2exit_rec(lev+1,actions,next_sq)
        if path_len >= 0:
          mark[sq] = next_sq
          path_len += 1
          actions.append(MazeAction(sq,ActionKind.MARK_RETURN,lev,\
                                    next_sq,path_len))
          break
      if path_len == -1:
        actions.append(MazeAction(sq,ActionKind.RETURN,lev,None,path_len))
      return path_len
    actions = list()
    path_len = somepath2exit_rec(0,actions,startsquare)
    mark_history = mark_history_get(actions)
    for sq, mark_at in mark_history.items():
      print('% mark_history[{}] = {}'.format(sq,mark_at))
    square_part = 0.47
    print('''\\documentclass{beamer}
             \\usepackage[english]{babel}
             \\newcommand{\\InCcontext}{false}
             \\usepackage{LocalDefs}
             \\lstloadlanguages{Python}
             \\lstset{language=Python}
             \\begin{document}
             \\begin{frame}[fragile]{}
             \\begin{columns}''')
    print('\\begin{{column}}{{{}\\textwidth}}'.format(square_part))
    print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
    print('\\begin{scope}')
    draw_grid(self._num_rows,self._num_cols)
    self.show_matrix_grayblocks()
    print(make_dot(startsquare[0],startsquare[1],self.start_color()))
    print('\\node[anchor=west] at ({}, {}) {{\\tiny dirs=[down,up,left,right]}};'
            .format(self._num_cols+1,self._num_rows))
    print('\\node[anchor=west] at ({}, {}) {{\\scriptsize EXPL}};'
            .format(self._num_cols+1,self._num_rows-1))
    print('\\fill[red,anchor=west] ({}, {}) circle (10pt);'
            .format(self._num_cols+5,self._num_rows-1))
    print('\\node[anchor=west] at ({}, {}) {{\\scriptsize EXIT}};'
            .format(self._num_cols+1,self._num_rows-2))
    print('\\fill[green,anchor=west] ({}, {}) circle (10pt);'
            .format(self._num_cols+5,self._num_rows-2))

    for sq, mark_at in mark_history.items():
      for idx in range(1,len(mark_at)):
        val = mark_at[idx-1][1]
        print('\\only<{}-{}>{{{}}}'.format(1+mark_at[idx-1][0],mark_at[idx][0],
                                           mark2string(sq,val)))
      print('\\only<{}->{{{}}}'.format(1+mark_at[-1][0],
                                       mark2string(sq,mark_at[-1][1])))
    print('''\\end{scope}
             \\end{tikzpicture}
             \\Lstusetiny{MazeNoIndentSomePathToExit}
             \\end{column}''')
    print('\\begin{{column}}{{{}\\textwidth}}'.format(1.0 - square_part))
    print('''\\begin{tiny}
             \\begin{tabular}{@{}l}''')
    print('\\\\\n'.join(map(str,actions)))
    print('''\\end{tabular}
             \\end{tiny}
             \\end{column}
             \\end{columns}
             \\end{frame}
             \\end{document}''')

def parse_arguments():
  p = argparse.ArgumentParser()
  p.add_argument('--noheader',action='store_true',default=False,
                  help='do not show latex header, i.e. restrict to tikzpicture')
  p.add_argument('-g','--grayblocks',metavar='<square>',nargs='*',default=None,
                  help=('display image of maze using gray blocks, optionally '
                        'display square given as argument'))
  p.add_argument('-b','--binary',action='store_true',default=False,
                  help='display image of maze using binary matrix')
  p.add_argument('-m','--mini',action='store_true',default=False,
                  help='use miniatur version of maze')
  p.add_argument('-a','--allpaths',metavar='<square>',nargs='*',default=None,
                  help=('for all given squares enumerate all paths to exit; '
                        'if no argument is given, then iterate over all open '
                        'squares'))
  p.add_argument('-s','--shortestpath',metavar='<square>',nargs='*',
                 default=None,
                  help=('for square given as argument display a shortest path '
                        'to exit; if no argument is given, then iterate over '
                        'all open square'))
  p.add_argument('-n','--neighbors',metavar='<square>',nargs='*',default=None,
                  help=('for square given as argument enumerate all its '
                        'neighbors, including exits; if no argument is given, '
                        'then iterate over all valid squares'))
  p.add_argument('--somepath',metavar='<square>/iterations>',type=str,
                  default=None,
                  help=('for square given as argument return path to '
                        'exit, if it exists, second'))
  p.add_argument('--track',metavar='<square>',type=str,
                 help='track steps of path computation from given square')
  p.add_argument('--scale',type=float,default=0.3,metavar='<float>',
                  help='specify scaling factor of tikz output')
  p.add_argument('--depth_first',action='store_true',default=False,
                  help=('use depth first search instead of breadth first '
                        'search for shortest path computation'))
  p.add_argument('--test',action='store_true',default=False,
                  help=('run tests for shortest path computation'))
  p.add_argument('--origin',action='store_true',default=False,
                  help='show origin of matrix')
  args = p.parse_args()
  if (args.grayblocks is not None) and args.binary:
    sys.stderr.write('{}: options -g and -b exclude each other\n'
                     .format(sys.argv[0]))
    exit(1)
  return args

big_maze_rows = {
  0 : [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
  1 : [0,6,16,22],
  2 : [0,2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,20,22],
  3 : [0,2,4,10,12,18,20,22],
  4 : [0,2,4,5,6,7,8,10,12,14,15,16,17,18,20,22],
  5 : [0,2,10,12,14,20,22],
  6 : [0,2,6,7,8,9,10,12,14,15,16,18,20,22],
  7 : [0,2,4,6,12,16,18,20,22],
  8 : [0,2,4,5,6,8,9,10,12,13,14,16,18,20,22],
  9 : [0,2,8,14,18,20,22],
  10 : [0,2,3,4,5,6,8,10,11,12,14,15,16,17,18,20,22],
  11 : [0,8,10,12,20,22],
  12 : [0,2,3,4,5,6,8,10,11,12,14,15,16,17,18,19,20,22],
  13 : [0,6,8,14,20,22],
  14 : [0,2,3,4,6,8,9,10,11,12,13,14,16,17,18,20,22],
  15 : [0,2,6,16,18,20,22],
  16 : [0,2,4,6,7,8,10,12,13,14,15,16,18,20,22],
  17 : [0,2,4,8,10,12,18,20,22],
  18 : [0,2,4,5,6,7,8,10,12,14,15,16,18,20,22],
  19 : [0,2,10,12,14,20,22],
  20 : [0,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,22],
  21 : [0,22],
  22 : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
}

small_maze_rows = dict()
mini_rows = 6
mini_columns = 7
for row in range(mini_rows):
  if row == mini_rows-1:
    small_maze_rows[row] = list(range(mini_columns))
  elif row == 0:
    small_maze_rows[row] = list(range(mini_columns-2))
    small_maze_rows[row].append(mini_columns-1)
  elif row == 2:
    small_maze_rows[row] = [0,2,3,4,mini_columns-1]
  elif row == 3:
    small_maze_rows[row] = [0,2,4,mini_columns-1]
  else:
    small_maze_rows[row] = [0,mini_columns-1]

args = parse_arguments()
maze = Maze(small_maze_rows if args.mini else big_maze_rows)

def verify_path(path):
  assert path
  previous = path[0]
  for p in path[1:]:
    assert (previous[0] == p[0] and \
            (previous[1] + 1 == p[1] or previous[1] - 1 == p[1])) or \
           (previous[1] == p[1] and \
            (previous[0] + 1 == p[0] or previous[0] - 1 == p[0]))
    previous = p

if args.grayblocks is not None:
  if args.shortestpath and len(args.shortestpath) == 1:
    path = maze.shortest_path2exit(eval(args.shortestpath[0]))
    maze.show_tikz(True,args.noheader,args.origin,args.scale,path)
  elif args.somepath:
    startsquare, path = maze.somepath2exit_iter_args(args.somepath)
    if path is not None:
      maze.show_tikz(True,args.noheader,args.origin,args.scale,path)
  elif args.track:
    startsquare = eval(args.track)
    maze.somepath2exit_track(args.scale,startsquare)
    exit(0)
  else:
    if len(args.grayblocks) == 1:
      maze.show_tikz(True,args.noheader,args.origin,args.scale,
                     [eval(args.grayblocks[0])])
    else:
      maze.show_tikz(True,args.noheader,args.origin,args.scale,args.grayblocks)
elif args.binary:
  maze.show_tikz(False,args.noheader,args.origin,args.scale)
elif args.allpaths is not None:
  if len(args.allpaths) > 0:
    for startsquare_string in args.allpaths:
      paths = maze.paths2exit(eval(startsquare_string))
      print('{}->{}'.format(startsquare_string,paths))
  else:
    for startsquare in maze.open_squares():
      paths = maze.paths2exit(startsquare)
      print('{}->{}'.format(startsquare,paths))
elif args.shortestpath is not None:
  if len(args.shortestpath) > 0:
    for startsquare_string in args.shortestpath:
      path = maze.shortest_path2exit_itrtv(eval(startsquare_string),
                                           args.depth_first)
      print('{}\t{}\t{}'.format(startsquare_string,len(path),path))
  else:
    for startsquare in maze.open_squares():
      path = maze.shortest_path2exit_itrtv(startsquare,args.depth_first)
      if args.test:
        path_rec = maze.shortest_path2exit(startsquare)
      if path is not None:
        if args.test:
          assert len(path) == len(path_rec)
        print('{}\t{}\t{}'.format(startsquare,len(path),path))
        min_dist2, path2 = maze.shortest_path2exit2(startsquare)
        verify_path(path2)
        assert min_dist2 + 2 == len(path)
        min_dist3, path3 = maze.shortest_path2exit3(startsquare)
        verify_path(path3)
        assert min_dist3 + 2 == len(path)
      elif args.test:
        assert path_rec is None
elif args.somepath:
  startsquare, path = maze.somepath2exit_iter_args(args.somepath)
  if path is not None:
    print('{}\t{}\t{}'.format(startsquare,len(path),path))
elif args.neighbors:
  if len(args.neighbors) > 0:
    for square_string in args.neighbors:
      neighbors_list = maze.neighbors(eval(square_string))
      print('{}\t{}'.format(square_string,neighbors_list))
  else:
    for square in maze.open_squares():
      neighbors_list = maze.neighbors(square)
      print('{}\t{}'.format(square,neighbors_list))

'''
def has_path2exit(square):
  if exit_square(square):
    return True
  else:
    return has_path2exit(square + (0,-1)) or   # down
           has_path2exit(square + (0,1)) or    # up
           has_path2exit(square + (-1,0)) or   # left
           has_path2exit(square + (1,0))       # right
def somepath2exit(self,start):
  mark = dict()
  def somepath2exit_rec(sq):
    if self.isexit(sq):
      mark[sq] = EXIT
      return 0
    if sq in mark and mark[sq] == EXPL:
      return -1
    mark[sq] = EXPL
    pathlen = -1
    for next_sq in self.neighbors(sq):
      pathlen = somepath2exit_rec(next_sq)
      if pathlen >= 0:
        mark[sq] = next_sq
        pathlen += 1
        break
    return pathlen
  pathlen = somepath2exit_rec(start)
  if pathlen < 0: return None
  return pathlen, mark
'''
