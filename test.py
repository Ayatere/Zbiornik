class Fluid:
    Q = 0
    Ca = 0

    def __init__(self, q, ca):
        self.Q = q
        self.Ca = ca


class Tank:
    A = 0
    H = 0
    V = 0
    Ca = 0

    def __init__(self, a, h, v, ca):
        self.A = a
        self.H = h
        if v > self.A * self.H:
            self.V = self.A * self.H
        else:
            self.V = v
        self.Ca = self.V * ca

    def calc(self, fluids, output):
        for i in fluids:
            self.V += i.Q
        self.V += output.Q


class Output:
    Q = 0

    def __init__(self, q):
        self.Q = q


tank = Tank(100, 10, 500, 1)
fluids = [Fluid(10, 1)]
output = Output(-5)

for i in range(10):
    tank.calc(fluids, output)
    print(tank.V)
