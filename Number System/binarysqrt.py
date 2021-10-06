#Calculate Sqrt by using binary search
def sqRoot(n):
    if(n ==0 or n ==1):
        return n
    start =1
    end =n
    while(start <=end):
        mid = (start+end)//2
        if (mid*mid == n):
            return mid
        if (mid*mid < n):
            start= mid+1
            ans = mid
        else:
            end =mid-1
    return ans

print(sqRoot(17))