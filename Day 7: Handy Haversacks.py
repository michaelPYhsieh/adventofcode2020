class Sol_DS:

    class Bag:  # like double linked list
        def __init__(self):
            self.contains = {}
            self.holds = set()
        # def __repr__(self):
        #     return '<contains:'+str(self.contains) +'; holds:'+ str(self.holds)+'>'

    def __init__(self):
        self.bags = {}
        fn = 'inputD7.txt'
        with open(fn, mode='r') as f:
            data = f.read()
        for d in data.split('\n'):
            self.add_rule(d)

    def put(self, bag_name, b_name, amt):
        for b in [bag_name, b_name]:
            if b not in self.bags:
                self.bags[b] = self.Bag()
        self.bags[bag_name].contains[b_name] = int(amt)
        self.bags[b_name].holds.add(bag_name)

    def add_rule(self, rule: str):
        for rm in [' bags', ' bag', '.']:
            rule = rule.replace(rm, '')
        bag_name, contains = rule.split(' contain ')
        if contains == 'no other':
            return
        contains = contains.split(', ')
        for c in contains:
            amt, b_name = c.split(' ', 1)
            self.put(bag_name=bag_name, b_name=b_name, amt=amt)

    def part1(self):
        s = self.bags['shiny gold'].holds
        q = list(s)
        while q:
            f = q[0]
            for b in self.bags[f].holds:
                s.add(b)
                q.append(b)
            q.pop(0)
        return len(s)

    def part2(self):
        re = -1
        q = {'shiny gold': 1}
        while q:
            nxt = {}
            for b, a in q.items():
                re += a
                for k, v in self.bags[b].contains.items():
                    nxt[k] = nxt.get(k, 0) + a*v
            q = nxt
        return re

    # def __repr__(self):
    #     return str(self.bags)


s = Sol_DS()

p = s.part1()
print('part1', p)
# part1 4

p = s.part2()
print('part2', p)
# part2 11310
