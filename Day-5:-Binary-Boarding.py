class Sol:
    def __init__(self):
        with open('inputD5.txt', mode='r') as f:
            data = f.read()
        self.data = data.split('\n')
    
    def chk(self):
        maxval = 0
        for d in self.data:
            maxval = max(maxval, self.fblr(d))
        return maxval
            
    def fblr(self, d):
        fb, lr = d[:7], d[-3:]
        fb = self._to_bin_to_int(fb, 'F', 'B')
        lr = self._to_bin_to_int(lr, 'L', 'R')
        return fb*8+lr
    
    def _to_bin_to_int(self, string, zero, one):
        string = string.replace(zero,'0').replace(one, '1')
        return int(string, 2)

    def chk2(self):
        s = set()
        for d in self.data:
            s.add(self.fblr(d))
        minval, maxval = min(s), max(s)
        r = set(range(minval, maxval+1))
        re = list(r-s)[0]
        return re


t = Sol().chk()
print('Sol1', t)
# Sol1 953

t = Sol().chk2()
print('Sol2', t)
# Sol2 615

