n = int(input("Enter the number : "))

m = ["", "M", "MM", "MMM"]
c = ["", "C", "CC", "CCC", "CD", "D",
    "DC", "DCC", "DCCC", "CM"]
x = ["", "X", "XX", "XXX", "XL", "L",
    "LX", "LXX", "LXXX", "XC"]
i = ["", "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX"]

thousands = m[n//1000]
hundreds = c[(n%1000)//100]
tens = x[(n%100)//10]
ones = i[n%10]

ans= (thousands+hundreds+tens+ones)
print(ans)