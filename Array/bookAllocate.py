#Book allocation Problem --> Allocate minimum number of pages
def minPages(arr, key):
    mn = max(arr)
    mx = sum(arr)
    res = 0
    while(mn<=mx):
        mid =(mn+mx)//2
        if(isFeasible(arr, key, mid)):
            res=mid
            mx =mid-1
        else:
            mn =mid+1
    return res
def isFeasible(arr, key, res):
    student, sum = 1, 0
    for i in range(len(arr)):
        if (sum+arr[i]>res):
            student+=1
            sum =arr[i]
        else:
            sum+=arr[i]
    return student <= key

arr= [10,20,10,30]
key = 2
print(minPages(arr, key))