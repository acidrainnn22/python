import itertools
s=input()
l=list(itertools.permutations(list(s)))
for i in l:
    print("".join(list(i)))