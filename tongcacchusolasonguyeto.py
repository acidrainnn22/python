from math import sqrt


def nt(n) :
    for i in range(2,int(sqrt(n))+1) :
        if n % i == 0 : return False 
    return n > 2

t = int(input())

while t > 0  :
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if nt(sum) : print("YES")
    else : print("NO")
    t-=1