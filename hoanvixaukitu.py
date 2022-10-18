a =[1]*10
used = [0]*10
s = input()
n = len((s))
def hienthi() :
    for i in range(n):
        print(s[a[i]], end ="")
    print()

def Try(i) :
    for j in range(n) :
        if used[j] == 0 :
            used[j] = 1
            a[i] = j
            if i == n -1 : hienthi()
            else : Try(i+1)
            used[j] = 0



Try(0)