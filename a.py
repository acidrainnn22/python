class thi():
    def __init__(self):
        self.ma = input()
        self.name = input()
        self.form = input()
t = int(input())
lst = []
for c in range(t):
    a = thi()
    lst.append(a)
lst = sorted(lst,key=lambda x: x.ma)
for c in lst:
    print(c.ma,c.name,c.form)