#find the number of ways in NxM matrix using recursion
def count(N, M):
    if (N==1 or M==1):
        return 1
    return count(N-1, M)+count(N, M-1)
print("There are",count(4, 3),"ways to traverse the matrix of 4x3")