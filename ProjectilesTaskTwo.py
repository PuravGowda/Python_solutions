import matplotlib.pyplot as plt
import math as m


def radians(deg):
    return deg * m.pi / 180


x = []
y = []
theta = radians(45)
d = [0, 0]
u = 50
v = [u * m.cos(theta), u * m.sin(theta)]
g = 10
res = 50
initial_height = 2
r = (u*m.sin(theta) + u*m.cos(theta)*m.sqrt((m.tan(theta)**2)+(2*g*initial_height/u*m.cos(theta))))/g

def y_pos(x):
    return -((g/(2*u*m.cos(theta)))*(x**2))+(m.tan(theta)*x)+initial_height

for i in range(res):
    x.append(i*r/res)
    y.append(y_pos(i*r/res))

plt.plot(x, y)

plt.xlabel("X (m)")
plt.ylabel("Y (m)")

plt.show()

