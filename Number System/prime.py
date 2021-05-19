#check the number is prime or not
def checkPrime(N):
    if N<2:
        return False
    else:
        for i in range(2, int(N/2)-1):
            if(N%i==0):
                return False
                break
        return True
print(checkPrime(100))