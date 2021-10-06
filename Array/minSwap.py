#Program to find the minimum number of swap to sort the array
def minSwap(arr, N):
    ans=0
    temp=arr.copy()
    temp.sort()
    for i in range(N):
        if arr[i]!=temp[i]:
            ans+=1
            swap(arr, i, indexOf(arr, temp[i]))
    return ans

def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def indexOf(arr, ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
        return -1
arr=[1, 4, 2, 5, 3]
n =len(arr)
print(minSwap(arr, n),"swaps are required to sort the array.")