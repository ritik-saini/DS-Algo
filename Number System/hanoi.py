#Tower of Hanoi problem in Python
def TOH(n, beg, aux, dest):
    if n > 0:
        TOH(n-1, beg, dest, aux)
        print("Move disk",n,"from",beg,"to",dest)
        TOH(n-1, aux, beg, dest)
n = int(input('Enter number of disk : '))
print()
TOH(n,'A','B','C') 