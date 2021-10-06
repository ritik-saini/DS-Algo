# Selection sort algorithm to sort the array
arr= [4,1,9,2,3,6]
n =len(arr)
for i in range(0, n-1):
    min =i
    for j in range(i+1, n):
        if arr[j]<arr[min]:
            min=j
    if min != i:
        arr[min], arr[i]=arr[i], arr[min]
    print(arr) #step by step sort