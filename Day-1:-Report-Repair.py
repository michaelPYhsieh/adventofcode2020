from copy import deepcopy
from numpy import prod # I'm lazy

class Sol:

    def __init__(self):
        with open('inputD1.txt', 'r') as f:
            data = f.read()
        data=data.split('\n')
        self.data = [int(x) for x in data]

    def nSum(self, n, sumval):
        dic = {():sumval}
        for i in range(len(self.data)):
            a = self.data[i]
            tmp = deepcopy(dic)
            for k, v in dic.items():
                left = v-a
                if left>=0 and len(k)<n:
                    tmp[k+(i,)] = left
            dic = tmp
        eq = {k:[self.data[a] for a in k] for k in dic if not dic[k] and len(k)==n}
        re = []
        for k, v in eq.items():
            re.append(prod(v))
        if not len(re)-1:
            return re[0]
        else:
            return re

t = Sol().nSum(2, 2020)
print('Sol1:', t)
# 926464

t = Sol().nSum(3, 2020)
print('Sol2:', t)
# 65656536

