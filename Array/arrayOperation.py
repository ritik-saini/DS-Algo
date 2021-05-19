#All the basic operation on array with Python

import array as arr
a=arr.array('d', [1.2,3.4,4.5,5.6])
print(len(a))
a.append(6.7)
#print(a)
a.extend([7.8,8.9,9.0])
#print(a)
a.insert(1,2.3)
print(a)
# a.pop()
# print(a)
# a.pop(3)
# print(a)
# a.remove(6)
# print(a)
b=arr.array('d', [1.3,3.5,4.6,5.7])
c= a+b
print(c)
#slicing
print(c[8:12])