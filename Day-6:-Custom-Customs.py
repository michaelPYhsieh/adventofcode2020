class Sol:
    def __init__(self):
        with open('inputD6.txt', mode='r') as f:
            data = f.read()
        data = data.split('\n'*2)
        self.data = data

    def chk1(self):
        re = 0
        for g in self.data:
            g = set(g.replace('\n', ''))
            re += len(g)
        return re
    
    def chk2(self):
        re = 0
        for g in self.data:
            ps = g.split('\n')
            s = set(ps[0])
            for p in ps[1:]:
                s &= set(p)
            re += len(s)
        return re


t = Sol().chk1()
print('Sol1', t)
# Sol1 6930

t = Sol().chk2()
print('Sol2', t)
# Sol2 3585
