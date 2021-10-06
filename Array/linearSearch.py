#find an element in array using linear search
arr =[10,6,8,14,12]
x=8
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
print('The index of element is '+str(linearSearch(arr, x)))