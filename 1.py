#Первая 

eps = float(input())
x = float(input())
S = 0
n = 0
fact = 1 

while (1):
    tmp = 5*(3*n**2 - 2)
    fact *= tmp
    c = (-1)**(n-1) * x**tmp / fact
    if (c > eps):
        S += c
    else:
        break
    n += 1 

print(S)
