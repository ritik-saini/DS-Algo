# Insertion sort algorithm to sort the array
arr= [8,4,1,5,9,2]
n = len(arr)
for i in range(1, n):
    temp, j = arr[i], i-1 # store the element in temp first
    while j>=0 and arr[j]>temp:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1]= temp
print(arr)