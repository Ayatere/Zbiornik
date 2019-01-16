from tank import Tank
from fluid import Fluid
from output import Output
import time
import matplotlib.pyplot as plt

tank = Tank(10000, 10, 500, 0.5)
fluids = [Fluid(60, 0.5), Fluid(250, 0.2)]
output = Output(-200)
dTime = time.time()

dataV = []
dataCa = []
iterations = 100
for x in range(iterations):
    tank.calc(fluids, output)
    dataV.append(tank.V)
    dataCa.append(tank.Ca)

plt.figure(1, figsize=(8, 3))
plt.grid(True)
plt.subplot(121)
plt.xlabel('Time')
plt.ylabel('Volume')
plt.plot(range(iterations), dataV, 'r')
plt.subplot(122)
plt.xlabel('Time')
plt.ylabel('Concentration of alcohol')
plt.plot(range(iterations), dataCa, 'b--')
plt.suptitle('Categorical Plotting')
plt.show()