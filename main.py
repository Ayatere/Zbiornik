import tank
import fluid
import output

tank = tank.Tank(100, 10, 500, 0.5)
fluids = [fluid.Fluid(10, 0.7),fluid.Fluid(40,0.1)]
output = output.Output(-50)
print(tank.A)
for i in range(10):
    tank.calc(fluids, output)
    print(tank.V, tank.Ca)
