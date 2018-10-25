from tank import Tank
from fluid import Fluid
from output import Output
import time
import msvcrt

tank = Tank(1000, 10, 500, 0.5)
fluids = [Fluid(190, 0.7), Fluid(10, 0.1)]
output = Output(-150)
dTime = time.time()
while True:
    if msvcrt.kbhit():
        print(ord(msvcrt.getch()))
        if ord(msvcrt.getch()) == 27:
            break
    if time.time() - dTime > 0.1:
        dTime = time.time()
        tank.calc(fluids, output)
        print(tank.V, tank.Ca)
    time.sleep(0.01)
