#rotate the array in clockwise direction by the no. of rotaion simple method
A = []
n = int(input('Enter no. of elements -> '))
d = int(input('Enter no. of elements which you want to rotate -> '))
print('Enter Elements -> ')
for i in range(n):
    A.append(int(input()))

def rotateArray(A, n, d):
    for i in range(d):
        temp = A[0]
        for j in range(len(A)-1):
            A[j]=A[j+1]
        A[len(A)-1] = temp

    for i in range(len(A)):
        print(A[i], end= ' ')

rotateArray(A, n, d)
