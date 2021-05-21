#famous problem - in which a circle of some members and they will shoot each other last one is the winner.
def jos(k, n): #k is the number of person and n is the range for shoot
    if n == 1:
        return 0
    return (jos(n-1, k)+k)%n
print (jos(6, 4),"is the winner.")