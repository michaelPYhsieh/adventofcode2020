class Sol1:
    def __init__(self):
        with open('inputD3.txt', 'r') as f:
            data = f.read()
        self.data = data.split('\n')
        self.cols, self.rows = len(self.data[0]), len(self.data)
        self.c, self.r = 0, 0
        self.re = 0

    def chk(self, right, down):
        while True:
            for i in range(right):
                self.c = (self.c+1) % self.cols
            for i in range(down):
                self.r += 1
            if not self.r < self.rows:
                break
            if self.data[self.r][self.c] == '#':
                self.re += 1
        return self.re


class Sol2:
    def __init__(self):
        self.re = 1

    def chk(self, arr):
        for r, d in arr:
            tmp = Sol1().chk(r, d)
            self.re *= tmp
        return self.re


arr = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
t = Sol2().chk(arr)
print('Sol2:', t)
# Sol2: 3316272960

t = Sol1().chk(3, 1)
print('Sol1:', t)
# Sol1: 203
