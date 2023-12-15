matrix_A=[]

for i in range(int(input('Enter no. of coordinates: '))):
    inp_str='Enter x and y coordinates separated by a space: '
    coord=list(map(int,input(inp_str).split()))
    coord.append(1)
    matrix_A.append(coord)

cx=int(input('Enter scaling variable cx: '))
cy=int(input('Enter scaling variable cy: '))

matrix_B=[[cx,0,0],[0,cy,0],[0,0,1]]

ans_matrix=[[0,0,0] for i in range(len(matrix_A))]

for row in range(len(matrix_A)):        # matrix multiplication algo
    for column in range(len(matrix_B[0])):
        for element in range(len(matrix_B)):
            ans_matrix[row][column]+=matrix_A[row][element]*matrix_B[element][column]

ans=[]
print('First two columns of each row:')
for i in ans_matrix:
        print([i[0],i[1]])