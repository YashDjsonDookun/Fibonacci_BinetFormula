import math

n = int(input("input n: "))
fib = []

def fib_num(n):
    f = ((((1+math.sqrt(5)))**n)-((1-math.sqrt(5))**n))/((2**n)*math.sqrt(5))
    return int(f)

for i in range(n+1):
    fib.append(fib_num(i))

print(fib)
