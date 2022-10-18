from math import gcd

n, m = [int (x) for x in input().split()]

for j in range(n, m) :
    for k in range(j+1, m):
        for x in range(k+1,m+1):
            if gcd(k, j) == 1 and gcd(j, x) == 1 and gcd(k, x) == 1:
                print('({},{},{})'.format(j,k,x))