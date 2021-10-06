def segregate(arr,size): 
    j = 0
    for i in range(size): 
        if (arr[i] <= 0): 
            arr[i], arr[j] = arr[j], arr[i] 
            j += 1 # increment count of non-positive integers 
    return j 


''' Find the smallest positive missing number 
in an array that contains all positive integers '''
def findMissingPositive(arr, size): 

    for i in range(size): 
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 
            
    for i in range(size): 
        if (arr[i] > 0): 
            
            # 1 is added because indexes start from 0 
            return i + 1
    return size + 1


def findMissing(arr, size): 
    
    # First separate positive and negative numbers 
    shift = segregate(arr, size) 
    
    # Shift the array and call findMissingPositive for 
    # positive part 
    return findMissingPositive(arr[shift:], size - shift)
arr = [1, 5, 2, 3, 6]
print(findMissingPositive(arr, len(arr)))