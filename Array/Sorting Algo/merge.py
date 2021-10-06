def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        Left = arr[:mid]
 
        # into 2 halves
        Right = arr[mid:]
 
        # Sorting the first half
        mergeSort(Left)
 
        # Sorting the second half
        mergeSort(Right)
 
        i = j = k = 0
 
        # Copy data to temp arrays Left[] and Right[]
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
 
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    