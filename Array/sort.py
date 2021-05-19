#Sort the given array
A = []
n = int(input('Enter number of elements : '))
print('Enter elements : ')
for i in range(n):
    A.append(int(input()))
A.sort(reverse= True)
print('Sorted array is :', A)