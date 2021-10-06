#Check the array is sorted or not?
A =[]
n = int (input('enter number of elements : '))
print('Enter elemets : ')
for i in range(0,n):
    A.append(int(input()))
def function(A):
    if len(A) ==1 or len(A) ==0:
        return True
    return A[0]<=A[1] and function(A[1:])
if function(A):
    print('yes, this is sorted')
else :
    print('No, this is not sorted')