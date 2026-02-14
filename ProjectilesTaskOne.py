import matplotlib.pyplot as plt
import math as m


def radians(deg):
    return deg*m.pi/180

x = []
y = []
theta = radians(45)
u = [0, 0]
v = [50*m.cos(theta), 50*m.sin(theta)]
g = 10
res = 50

for i in range(res):
    x.append(u[0])
    y.append(u[1])
    v[1] -= g/(res/10)
    u[0] += v[0]/(res/10)
    u[1] += v[1]/(res/10)

    
    
plt.plot(x, y)

plt.xlabel("X (m)")
plt.ylabel("Y (m)")

plt.show()
    
