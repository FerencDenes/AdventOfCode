input = [ line.split(' -> ') for line in open('20/input.txt').read().split('\n') ]

low = False
high = True

class Mod:
    def act(self, signal, src):
        pass
    def addInput(self, conn):
        pass

class Broadcaster(Mod):
    def __init__(self, conns):
        self.conns = conns
    def act(self, signal, src):
        return [ (c, signal) for c in self.conns]
    def addInput(self, conn):
        pass

class Conjunction(Mod):
    def __init__(self, conns, name):
        self.conns = conns
        self.state = {}
        self.prevSign = low
        self.name = name
        self.period = 0
    def act(self, signal, src):
        self.state[src] = signal
        sign = low
        for c in self.state:
            if self.state[c] == low:
                sign = high
                break
        if sign != self.prevSign:
            self.prevSign = sign
            if self.period == 0 and sign == low:
                self.period = i
        return [ (c, sign) for c in self.conns]
    def addInput(self, conn):
        self.state[conn] = low
    def getSignal(self):
        sign = low
        for c in self.state:
            if self.state[c] == low:
                sign = high
                break
        return sign


class FlipFlop(Mod):
    def __init__(self, conns):
        self.conns = conns
        # off
        self.state = low
    def act(self, signal, src):
        if signal == high:
            return []
        self.state = not self.state
        return [ (c, self.state) for c in self.conns]
    def addInput(self, conn):
        pass
    def getSignal(self):
        return self.state

class Dummy(Mod):
    def __init__(self, conns):
        pass
    def act(self, signal, src):
        if signal == low:
            print("part2", i)
        return []
    def addInput(self, conn):
        pass

mods = {}
for line in input:
    conns = line[1].split(', ')
    if line[0] == 'broadcaster':
        mods['roadcaster'] = Broadcaster(conns)
    elif line[0][0] == '&':
        mods[line[0][1:]] = Conjunction(conns, line[0][1:])
    elif line[0][0] == '%':
        mods[line[0][1:]] = FlipFlop(conns)
    for c in conns:
        # rx
        if c not in mods:
            mods[c] = Dummy([])

for line in input:
    conns = line[1].split(', ')
    for c in conns:
        mods[c].addInput(line[0][1:])

lows = 0
highs = 0
found = False
def push(i):
    global lows
    global highs
    global found
    pulses = []
    pulses.append(('roadcaster', low, None))
    while len(pulses) > 0:
        (dst, signal, src) = pulses.pop(0)
        # print(src, signal, dst)
        if signal == low:
            lows += 1
        else:
            highs += 1
        signals = mods[dst].act(signal, src)
            
        pulses.extend([ (dst2, signal, dst) for (dst2, signal) in signals])
        if dst == 'rx' and signal == low and not found:
            print(i)
            found = True

for i in range(1,1001):
    push(i)

print(lows * highs)


while i < 10000:
    i += 1
    push(i)

print(mods['qq'].period * mods['bc'].period * mods['bx'].period * mods['gj'].period)
