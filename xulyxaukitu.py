s1 = set(input().lower().split())
s2 = set(input().lower().split())
for i in sorted(s1|s2) :
    print(i, end = " ")
print()
for j in sorted(s1&s2) :
    print(j, end = " ")

