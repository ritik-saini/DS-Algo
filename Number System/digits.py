#count the digits of a number
import math
def numberDigit(n):
    count = int(math.log(n, 10)+1)
    # count = 0
    # while n!=0:
    #     n//=10
    #     count+=1
    return count
def countDigit(n):
    count = 0
    while n!=0:
        n//=10
        count+=1
    return count

print(numberDigit(55648964))
print(countDigit(98856))