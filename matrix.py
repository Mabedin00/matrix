"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row = ""
    for y in range(4):
        for x in range(len(matrix)):
            # print("x:{} y:{}".format(x, y))
            row += str(matrix[x][y]) + "   "
        row = row[:-1] + "\n"
    # print(matrix)
    print(row)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (x == y):
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0
#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	temp_col = [0,0,0,0]
	row = [0,0,0,0]
	length = len(m2)
	for col in range(length):
		for x in range(4):
			for y in range(4):
				row[y] = m1[x][y]
			temp_col[x] = multiply_r_and_c(row, m2[col])
		m2[col] = temp_col[:]
		
			
    




#helper function for matrix multiplication. Multiplies a row and a column
def multiply_r_and_c(row , col):
    output = 0;
    for x in range(4):
        output += row[x] * col[x]
    return output











def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
