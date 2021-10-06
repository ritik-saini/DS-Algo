#Search the element in array by using Binary Search
#*Binary search only works on sorted array*
def bianrySearch(arr, n, x):
    l=0
    r= n-1
    while(l<=r):
        mid = (l+r)//2
        if (arr[mid]==x):
            return mid
        if (arr[mid]<x):
            l=mid+1
        else:
            r=mid-1
    return -1
arr=[2,4,6,8,10,12]
n=len(arr)
x=10
print(bianrySearch(arr, n, x))