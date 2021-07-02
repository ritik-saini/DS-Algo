def modifyMatrix(mat):
    rowflag=False
    colflag=False

    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if (i==0 and mat[i][j]==1):
                rowflag = True

            if (j==0 and mat[i][j]==1):
                colflag = True

            if mat[i][j]==1:
                mat[0][j]=1
                mat[i][0]=1

    for i in range(1, len(mat)):
        for j in range(1, len(mat)+1):
            if mat[0][j]==1 or mat[i][0]==1:
                mat[i][j]=1

    if rowflag ==True:
        for i in range(0, len(mat)):
            mat[0][i]=1

    if colflag ==True:
        for i in range(0, len(mat)):
            mat[i][0]=1

def printMatrix(mat) :
     
    for i in range(0, len(mat)) :
        for j in range(0, len(mat) + 1) :
            print( mat[i][j], end = "" )
         
        print()
         
mat = [ [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0] ]
         
print("Input Matrix :")
printMatrix(mat)
     
modifyMatrix(mat)
     
print("Matrix After Modification :")
printMatrix(mat)