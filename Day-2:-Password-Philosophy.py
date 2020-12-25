with open('inputD2.txt', 'r') as f:
    data = f.read()
data = data.replace(':', '').replace('-',' ').split('\n')
data = [x.split(' ') for x in data]


def chk1(a, b, c, d):
    cnt = d.count(c)
    a, b = int(a), int(b)
    if a <= cnt <= b:
        return True
    else:
        return False


def chk2(a, b, c, d):
    a, b = int(a), int(b)
    s = [d[a-1], d[b-1]]
    s = set(s)
    if len(s) > 1 and c in s:
        return True
    else:
        return False


re = 0
for a, b, c, d in data:
    if chk1(a, b, c, d):
        re += 1
print('Sol1:', re)
# Sol1: 660


re = 0
for a, b, c, d in data:
    if chk2(a, b, c, d):
        re += 1
print('Sol2:', re)
# Sol2: 530

