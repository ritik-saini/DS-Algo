# Quick sort algorithm to sort the array
# time complexity O(nlogn)
def partition(arr, low, high): #partioning logic of array
    pivot = arr[low]
    i, j =low, high
    while(i<j):
        while (i <len(arr) and arr[i]<=pivot):
            i+=1
        while (arr[j]>pivot):
            j-=1
        if(i<j):
            arr[j], arr[i]= arr[i], arr[j]
    arr[j], arr[low]= arr[low], arr[j]
    return j

def quickSort(arr, low, high): #sorting algo
    if low<high:
        p= partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
    return arr

arr = [ 10, 7, 8, 9, 1, 5 ]
low, high = 0, len(arr)-1
print(quickSort(arr, low, high))