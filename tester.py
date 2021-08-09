class thing(object):
    def __init__(self,n,m):
        self.m=m
        self.n=n

class num(thing):
    def __init__(self, j,k,n,m):
        self.k=k
        self.j=j
        thing.__init__(self, n, m)

x=num(1,2,3,4)
print(x.m)