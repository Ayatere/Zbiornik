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
        self.Ca = ca

    def calc(self, fluids, output):
        for fluid in fluids:
            if self.V + fluid.Q + output.Q > self.A * self.H:
                self.V -= fluid.Q
            else:
                self.Ca = (self.V * self.Ca + fluid.Q * fluid.Ca) / (self.V + fluid.Q)
            self.V += fluid.Q
        if self.V + output.Q > 0:
            self.V += output.Q
        else:
            self.V = 0
            self.Ca = 0
