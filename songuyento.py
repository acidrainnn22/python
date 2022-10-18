def nt(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return 0
    return 1
t=int(input())
for i in range(t):
    n=int(input())
    print("YES" if nt(n)==1 else "NO")