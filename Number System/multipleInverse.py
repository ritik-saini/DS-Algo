class Solution:    
    def modInverse(self,a,m):
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1
 
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        am=[int(x) for x in input().strip().split()]
        a=am[0]
        m=am[1]
        ob=Solution()
        print(ob.modInverse(a,m))
        
        
        T-=1
    
    


if __name__=="__main__":
    main()