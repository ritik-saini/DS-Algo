#Using slide window technique calculate the maxsum of sub array
def maxSum(arr, n, k):
    if (n<k):
        print("Invalid")
        return -1
    res =0 
    for i in range (k):
        res+=arr[i]
    curr_sum = res
    for i in range(k, n):
        curr_sum+=arr[i]-arr[i-k]
        res = max(curr_sum, res)
    return res

arr=[]
n = int(input('Enter size of array : '))
print('Enter element of Array :')
for i in range(n):
    arr.append(int(input()))
k = int(input('Enter size of window : '))
print(maxSum(arr, n, k))