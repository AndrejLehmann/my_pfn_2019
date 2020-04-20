#!/usr/bin/env python3

import numpy as np

def show_matrix(rows,columns,marked=None):
  def index2rowcol(idx):
    row = idx // rows
    column = idx - row * columns
    return row, column
  print(\
'''\begin{{center}}
  \begin{{tikzpicture}}[baseline=-\the\dimexpr\fontdimen22\textfont2\relax ]
  \matrix (m)[matrix of math nodes,left delimiter=(,right delimiter=)]
  {{
''')
  for i in range(rows):
    from_col = i * columns
    to_col = (i+1) * columns
    print('{}\\\\'.format(' & '.join(map(str,list(range(from_col,to_col))))))
  print('};')
  if not (marked is None):
    print('\\begin{pgfonlayer}{myback}')
    for idx in marked:
      row, column = index2rowcol(idx)
      print('\\node[fit=(m-{}-{}),rounded corners,fill=black!10,scale=0.6]{{}};'
             .format(row+1,column+1))
    print('\\end{pgfonlayer}')
  print('\\end{tikzpicture}')
  print('\\end{center}')

print('# npXDimArray')
one_dim_array = np.array([0.0, 1.0, 2.0, 3.0])
two_dim_array = np.array([[0, 1, 2], [3, 4, 5]])
print('one_dim_array=\n{}'.format(one_dim_array))
print('two_dim_array=\n{}'.format(two_dim_array))

print('# npXDimArrayDtype')
print('one_dim_array.dtype={}'.format(one_dim_array.dtype))
print('two_dim_array.dtype={}'.format(two_dim_array.dtype))

print('# npXDimArrayDim')
print('one_dim_array.ndim={}'.format(one_dim_array.ndim))
print('two_dim_array.ndim={}'.format(two_dim_array.ndim))

print('# npXDimArrayShape')
print('one_dim_array.shape={}'.format(one_dim_array.shape))
print('two_dim_array.shape={}'.format(two_dim_array.shape))

print('# npXDimArrayLen')
print('len(one_dim_array)={}'.format(len(one_dim_array)))
print('len(two_dim_array)={}'.format(len(two_dim_array)))

print('# npXDimArrayEvenly')
one_dim_array_int = np.arange(10)
one_dim_array_float = np.linspace(0,1,6) # first, last, num entries
print('one_dim_array_int=\n{}'.format(one_dim_array_int))
print('one_dim_array_float=\n{}'.format(one_dim_array_float))

print('# npMatrixOnes')
onesmatrix = np.ones((3, 3))
print('onesmatrix=\n{}'.format(onesmatrix))

print('# npMatrixZeros')
zerosmatrix = np.zeros((2, 3))
print('zerosmatrix=\n{}'.format(zerosmatrix))

print('# npMatrixEye')
maindiag1matrix = np.eye(3)
print('maindiag1matrix=\n{}'.format(maindiag1matrix))

print('# npMatrixMainDiagSet')
maindiagsetmatrix = np.diag(np.array([1, 2, 3, 4]))
print('maindiagsetmatrix=\n{}'.format(maindiagsetmatrix))

print('# npMatrixOnesWithTwoSet')
matrix1 = np.ones((4,4),
                  dtype=int)
matrix1[2,3] = 2
matrix1[3,1] = 6

print('# npMatrixMainDiagShift')
maindiagonal = np.linspace(1,4,4)
matrix_main_diag = np.diag(maindiagonal)
matrix_main_diag_shift = np.delete(matrix_main_diag,axis=1,obj=0)

print('# npMatrixTiled')
firstline = np.tile([4,3],3)
secondline = np.tile([2,1],3)
matrix_tiled = np.array(np.tile([firstline,secondline],(2,1)))
print(matrix_tiled)  # outputs matrix shown at top left

print('# npOneDimSliced')
onedimarray = np.arange(10)   # [0 1 2 3 4 5 6 7 8 9]
onedimarray_sliced = onedimarray[2:9:3] # start:end(exclusive):step
print(onedimarray_sliced)

square_matrix = np.arange(25).reshape(5,5)
print(square_matrix)

print('# npMatrixonfirstrow')
onfirstrow = square_matrix[0,3:5]
print(onfirstrow)

print('# npMatrixSouthEast')
south_east22 = square_matrix[3:,3:]
print(south_east22)

print('# npMatrixColumnthree')
column3 = square_matrix[:,2]
print(column3)

print('# npMatrixScattered')
scattered = square_matrix[2::2,::2]
print(scattered)

print('# npOneDimArraySliceisView')
arr = np.arange(8)
arr_step2 = arr[::2]
arr_step2[0] = 12
print('arr={}'.format(arr))
print('arr_step2={}'.format(arr_step2))

print('# npOneDimArrayPlusOne')
arr = np.arange(4)
arr_plus1 = arr + 1
print(arr_plus1)

print('# npOneDimArrayTwoExp')
arr = np.arange(9)
twoexponents = 2 ** arr
print(twoexponents)

print('# npOneDimArrayScalar')
summand1 = np.array([3,2,4,7])
summand2 = np.array([5,4,4,1])
sumof = summand1 + summand2
difference = summand1 - summand2
simpleproduct = summand1 * summand2
equality = summand1 == summand2
print('sumof={}'.format(sumof))
print('difference={}'.format(difference))
print('simpleproduct={}'.format(simpleproduct))
print('equality={}'.format(equality))

print('# npMatrixmult')
matrix1 = np.array([[3,2,1],[1,0,2]])
matrix2 = np.array([[1,2],[0,1],[4,0]])
matrixproduct = matrix1.dot(matrix2)
print('matrixproduct=\n{}'.format(matrixproduct))

print('# npTranspose')
uppertriangular = np.triu(np.ones((3, 3),dtype=int), 1)
lowertriangular = uppertriangular.T
print('uppertriangular=\n{}'.format(uppertriangular))
print('lowertriangular=\n{}'.format(lowertriangular))

print('# npArraySumOneDim')
arr = np.arange(1,6)
print('sum(arr)={}'.format(np.sum(arr)))

print('# npArraySumTwoDim')
matrix = np.array([[1,1],[2,2]])
print('col: sum(matrix,axis=0)={}'.format(np.sum(matrix,axis=0)))
print('row: sum(matrix,axis=1)={}'.format(np.sum(matrix,axis=1)))

print('# npMinMax')
arr = np.array([2,3,2,8,7,3,4,1])
print('min(arr)={}'.format(np.min(arr)))
print('max(arr)={}'.format(np.max(arr)))

print('# npArgMinMax')
arr = np.array([2,3,2,8,7,3,4,1])
print('argmin(arr)={}'.format(np.argmin(arr)))
print('argmax(arr)={}'.format(np.argmax(arr)))

print('# npMeanMedianStd')
arr = np.array([2,3,2,8,7,3,4,1])
print('mean(arr)={}'.format(np.mean(arr)))
print('median(arr)={}'.format(np.median(arr)))
print('std(arr)={:.2f}'.format(np.std(arr)))

population = np.loadtxt('Math/population.tsv')
years, hares, lynxes, carrots = population.T


import matplotlib.pyplot as plt
plt.switch_backend('agg')
fig, ax = plt.subplots()
ax.set_xticks(np.arange(min(years), max(years)+1, 2))
ax.plot(years, hares, years, lynxes, years, carrots)
ax.set_title(('Population of different species in northern Canada'
              'from {}-{}').format(int(min(years)),int(max(years))))
ax.legend(('Hares', 'Lynxes', 'Carrots'), loc='upper right')
fig.savefig('population.png')

print('# npPopMeanStd')
species_pop = population[:,1:]
popmean = np.mean(species_pop,axis=0)  # arr of 3 floats, 1 per col
popmed = np.median(species_pop,axis=0) # arr of 3 floats. 1 per col
popstd = np.std(species_pop,axis=0)    # arr of 3 floats, 1 per col
print('# species\tpmean\tpmedian\tpstd')
for species,pmean,pmed,pstd in zip(['hares','lynxes','carrots'],
                                    popmean,popmed,popstd):
  print('{}\t{:.0f}\t{:.0f}\t{:.0f}'
         .format(species,pmean,pmed,pstd))

print('# npMatrixFlatten')
matrix = np.array([[1,2,3],[4,5,6]])
print('elements={}'.format(matrix.ravel()))

print('# npArrayReshape')
width = height = 4
arr = np.arange(width * height)
matrix = arr.reshape(width,height)
print('matrix=\n{}'.format(matrix))

np.random.seed(341433233)
fig, ax = plt.subplots()
ax.matshow(matrix,cmap='gist_ncar')
fig.savefig('colorgrid.png')
fig, ax = plt.subplots()
ax.matshow(np.random.rand(4,4),cmap='gist_ncar')
fig.savefig('rcolorgrid.png')

print('# npArrayResize')
arr = np.array([1,2,3,4])
arr.resize((8,))
matrix = np.ones((2,2),dtype=int)
matrix.resize(3,2)
print('arr={}'.format(arr))
print('matrix=\n{}'.format(matrix))

print('# npArrayReshapeTranspose')
arr = np.arange(1,16)
matrix = arr.reshape(3,5).T
submatrix = matrix[1:4:2,::]
print('matrix=\n{}'.format(matrix))
print('submatrix=\n{}'.format(submatrix))

print('# npPolynomialDeclare')
polynomial = np.poly1d([3, 2, -1])

print('polynomial order: {}'.format(polynomial.order))
print('solution of polynomial = 0: {}'.format(polynomial.roots))

print('')

#show_matrix(5,5)
show_matrix(5,5,onfirstrow.ravel())
show_matrix(5,5,south_east22.ravel())
show_matrix(5,5,column3.ravel())
show_matrix(5,5,scattered.ravel())

binexparr = np.arange(5)
binexparr = 2 ** binexparr
print(binexparr)

broad_a = np.tile(np.arange(0, 40, 10), (3, 1)).T
broad_b = np.array([0,1,2])

print(broad_a + broad_b)

reshape_ex = np.arange(1,16).reshape(3,5).T

print(reshape_ex)
