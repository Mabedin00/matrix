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

matrixT = [[2,1,0,7], [0,3,0,0], [0,0,4,0], [0,0,0,5]]
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

add_point(matrix2, 3, 5 , 1)
add_edge(matrix2, 40, 40, 0 ,460, 40, 0)

print("Points Added")
print_matrix(matrix2)

body_matrix = new_matrix()
body_matrix = body_matrix[4:] #removes initial 0
#add_edge( matrix, x0, y0, z0, x1, y1, z1 )
add_edge(body_matrix, 75, 100, 0, 1050, 100, 0)
add_edge(body_matrix, 1050, 100, 0, 1050, 250, 0)
add_edge(body_matrix, 1050, 250, 0, 125, 250, 0)
add_edge(body_matrix, 125, 250, 0, 200, 350, 0)
add_edge(body_matrix, 200, 350 , 0, 300, 350, 0)
add_edge(body_matrix, 300, 350 , 0, 400, 450, 0)
add_edge(body_matrix, 400, 450 , 0, 150, 450, 0)
add_edge(body_matrix, 150, 450 , 0, 25, 300, 0)
add_edge(body_matrix, 25, 300 , 0, 50, 200, 0)
add_edge(body_matrix, 50, 200 , 0, 75, 100, 0)

leg0_matrix = new_matrix()
leg0_matrix = leg0_matrix[4:]
add_edge(leg0_matrix, 150, 100, 0, 150, 0, 0)
add_edge(leg0_matrix, 150, 0, 0, 300, 0, 0)
add_edge(leg0_matrix, 300, 0, 0, 250, 50, 0)
add_edge(leg0_matrix, 250, 50, 0, 250, 100, 0)

leg1_matrix = new_matrix()
leg1_matrix = leg1_matrix[4:]
add_edge(leg1_matrix, 300, 100, 0, 300, 0, 0)
add_edge(leg1_matrix, 300, 0, 0, 450, 0, 0)
add_edge(leg1_matrix, 450, 0, 0, 400, 50, 0)
add_edge(leg1_matrix, 400, 50, 0, 400, 100, 0)

leg2_matrix = new_matrix()
leg2_matrix = leg2_matrix[4:]
add_edge(leg2_matrix, 550, 100, 0, 550, 0, 0)
add_edge(leg2_matrix, 550, 0, 0, 700, 0, 0)
add_edge(leg2_matrix, 700, 0, 0, 650, 50, 0)
add_edge(leg2_matrix, 650, 50, 0, 650, 100, 0)

leg3_matrix = new_matrix()
leg3_matrix = leg3_matrix[4:]
add_edge(leg3_matrix, 700, 100, 0, 700, 0, 0)
add_edge(leg3_matrix, 700, 0, 0, 850, 0, 0)
add_edge(leg3_matrix, 850, 0, 0, 800, 50, 0)
add_edge(leg3_matrix, 800, 50, 0, 800, 100, 0)

#
mouth_matrix = new_matrix()
mouth_matrix = mouth_matrix[4:]
mouth_color = [255, 0, 0]
add_edge(mouth_matrix, 775, 175, 0, 825, 150, 0)
add_edge(mouth_matrix, 825, 150, 0, 1050, 150, 0)


#draw_trinagles(matrix, height, width, x0, y, x1):
teeth_matrix = new_matrix()
teeth_matrix = teeth_matrix[4:]
add_trinagles(teeth_matrix, -25, 25, 850, 150,1050)
teeth_color = [255, 255, 255]

spikes_matrix = new_matrix()
spikes_matrix = spikes_matrix[4:]
add_trinagles(spikes_matrix, 50, 50, 200, 250, 600)

nose_matrix = new_matrix()
nose_matrix = nose_matrix[4:]
add_edge(nose_matrix, 1050, 250, 0, 1050, 275, 0)
add_edge(nose_matrix, 1050, 275, 0, 1025, 275, 0)
add_edge(nose_matrix, 1025, 275, 0, 1025, 250, 0)
add_edge(nose_matrix, 1025, 275, 0, 1000, 275, 0)
add_edge(nose_matrix, 1000, 275, 0, 1000, 250, 0)

eyes_matrix = new_matrix()
eyes_matrix = eyes_matrix[4:]
add_edge(eyes_matrix, 650, 250, 0, 650, 300, 0)
add_edge(eyes_matrix, 650, 300, 0, 700, 300, 0)
add_edge(eyes_matrix, 700, 300, 0, 700, 250, 0)
add_edge(eyes_matrix, 750, 250, 0, 750, 300, 0)
add_edge(eyes_matrix, 750, 300, 0, 800, 300, 0)
add_edge(eyes_matrix, 800, 300, 0, 800, 250, 0)





draw_lines( body_matrix, screen, color )
draw_lines( leg0_matrix, screen, color )
draw_lines( leg1_matrix, screen, color )
draw_lines( leg2_matrix, screen, color )
draw_lines( leg3_matrix, screen, color )
draw_lines( mouth_matrix, screen, mouth_color )
draw_lines( teeth_matrix, screen, teeth_color )
draw_lines( spikes_matrix, screen, color )
draw_lines( nose_matrix, screen, color )
draw_lines( eyes_matrix, screen, teeth_color )









#
display(screen)
