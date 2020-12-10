import inspect


class Sol:
    def __init__(self):
        with open('inputD4.txt', 'r') as f:
            data = f.read()
        data = data.replace(' ', '\n').split('\n'*2)
        data = [d.split('\n') for d in data]
        self.data = []
        for d in data:
            tmp = {}
            for t in d:
                tmp[t.split(':')[0]] = t.split(':')[1]
            self.data.append(tmp)

    def chk1(self):
        pass
        re = 0
        fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        for d in self.data:
            if not fields-set(d):
                re += 1
        return re

    def chk2(self):
        pass
        re = 0
        fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        for d in self.data:
            if not fields-set(d) and self.chks(d):
                re += 1
        return re

    def chks(self, d):
        # return self.chk_byr(d) and self.chk_iyr(d) and self.chk_eyr(d) and self.chk_hgt(d) and self.chk_hcl(d) and self.chk_ecl(d) and self.chk_pid(d)
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        methods = [x[1] for x in methods if x[0][:4] == 'chk_']
        for m in methods:
            if not m(d):
                return False
        return True

    def chk_pid(self, d):
        t = d['pid']
        return len(t) == 9 and t.isdigit()

    def chk_ecl(self, d):
        return d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def chk_hcl(self, d):
        t = d['hcl']
        sharp, color = t[0], t[1:]
        r = list(range(48, 58)) + list(range(97, 103))
        r = set([chr(a) for a in r])
        return sharp == '#' and len(color) == 6 and not any([c not in r for c in color])

    def chk_hgt(self, d):
        t = d['hgt']
        if len(t) < 4:
            return False
        num, unit = int(t[:-2]), t[-2:]
        return (unit == 'cm' and 150 <= num <= 193) or (unit == 'in' and 59 <= num <= 76)

    def chk_byr(self, d):
        t = d['byr']
        return t.isdigit() and 1920 <= int(t) <= 2002

    def chk_iyr(self, d):
        t = d['iyr']
        return t.isdigit() and 2010 <= int(t) <= 2020

    def chk_eyr(self, d):
        t = d['eyr']
        return t.isdigit() and 2020 <= int(t) <= 2030


t = Sol().chk1()
print('Sol1:', t)
# Sol1: 226

t = Sol().chk2()
print('Sol2:', t)
# Sol2: 160
