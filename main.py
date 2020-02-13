from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix1 = new_matrix()

z = 0
for x in range(4):
    for y in range(4):
        matrix1[x][y] = z
        z += 1
print("New Matrix1")
print_matrix(matrix1)
print("Identity of Matrix1")
ident(matrix1)

print_matrix(matrix1)

matrixT = [[2,0,3,0], [0,3,0,6], [0,7,4,0], [10,9,0,5]]
print("A new transformation Matrix Appeared!")
print_matrix(matrixT)

matrix2 = new_matrix(4,5)
for x in range(5):
    for y in range(4):
        matrix2[x][y] = z
        z += 1
print("Prepared to be Transformed Matrix2!")        
print_matrix(matrix2)

print("The transformation has been completed")
matrix_mult(matrixT, matrix2)
print_matrix(matrix2)


# draw_lines( matrix, screen, color )
# display(screen)
