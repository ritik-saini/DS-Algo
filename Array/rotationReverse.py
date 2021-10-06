#rotate the array in clockwise direction by the no. of rotaion using reversal method
def reverseArray(arr, start, end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end = end-1
def leftRotate(arr, d):
    if d==0:
        return
    n = len(arr)
    d= d%n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i], end=' ')
 

arr = []
n = int(input('Enter no. of elements -> '))
d = int(input('Enter no. of elements which you want to rotate -> '))
print('Enter Elements -> ')
for i in range(n):
    arr.append(int(input()))
 
leftRotate(arr, d)
printArray(arr)