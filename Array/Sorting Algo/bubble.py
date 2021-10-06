# Bubble sort algorithm to sort the array
# time complexity O(n^2)
arr= [4, 3, 7, 1, 5]
n= len(arr)
for i in range(0, n-1):
    swapped =False # For Optimiation
    for j in range(0, n-i-1):
        if arr[j+1]<arr[j]:
            swapped =True
            arr[j+1], arr[j]=arr[j], arr[j+1] #Swapping
    print(arr) #steps for sorting
    if not swapped :
        break