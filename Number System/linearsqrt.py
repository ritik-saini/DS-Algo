#calculate square root by using linear search
def sqRoot(a):
    if (a==0 or a==1):
        return a
    for i in range(a):
        if i*i == a:
            return i
        if i*i > a:
            return i-1
print(sqRoot(1))