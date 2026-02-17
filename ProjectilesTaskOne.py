import matplotlib.pyplot as plt
import math as m


def radians(deg):
    return deg*m.pi/180

x = []
y = []
theta = radians(45)
d = [0, 0]
u = 50
v = [u*m.cos(theta), u*m.sin(theta)]
g = 10
res = 50
initial_height = 2

for i in range(res):
    x.append(d[0])
    y.append(d[1])
    v[1] -= g/(res/10)
    d[0] += v[0]/(res/10)
    d[1] += v[1]/(res/10)

    
    
plt.plot(x, y)

plt.xlabel("X (m)")
plt.ylabel("Y (m)")

plt.show()
    
