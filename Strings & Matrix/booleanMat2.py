R = 3
C = 4
def modifyMatrix(mat):
    row = [0]*R
    col = [0]*C
    for i in range(0, R):
        row[i]=0

    for i in range(0, C):
        col[i]=0

    for i in range (0, R):
        for j in range(0, C):
            if mat[i][j]==1:
                row[i]= 1
                col[j]= 1

    for i in range (0, R):
        for j in range(0, C):
            if row[i]==1 or col[j]==1:
                mat[i][j]=1

def printMatrix(mat) :
    for i in range(0, R):         
        for j in range(0, C) :
            print(mat[i][j], end = " ")
        print()

mat = [ [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0] ]
 
print("Input Matrix n")
printMatrix(mat)
 
modifyMatrix(mat)
 
print("Matrix after modification n")
printMatrix(mat)