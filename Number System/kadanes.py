#Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
#Kadane's Algo
class Solution:
    def maxSubArraySum(self,a,size):
        maxSum = 0
        currSum = 0
        
        for i in range(size):
            currSum = currSum+a[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum
        ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()