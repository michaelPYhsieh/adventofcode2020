class Sol1:
    def __init__(self):
        with open('input.txt', 'r') as f:
            data = f.read()
        data = data.split('\n')
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.c, self.r = 0, 0
        self.re = 0

    def cnt(self):
        if self.r < self.rows and self.data[self.r][self.c] == '#':
            self.re += 1

    def right(self):
        self.c = (self.c+1) % self.cols

    def down(self):
        self.r += 1

    def chk(self, right, down):
        while self.r < self.rows:
            for i in range(right):
                self.right()
            for i in range(down):
                self.down()
            self.cnt()
        return self.re


class Sol2:
    def __init__(self, arr):
        self.arr = arr

    def chk(self):
        self.re = 1
        for r, d in self.arr:
            tmp = Sol1().chk(r, d)
            self.re *= tmp
        return self.re


arr = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
t = Sol2(arr).chk()
print('Sol2:', t)


t = Sol1().chk(3, 1)
print('Sol1:', t)
