import Backtracking
import GridGraphGen
import matplotlib.pyplot as plt
import numpy as np

#h = int(input("Enter height: "))
#w = int(input("Enter width:"))

h = 9
w = 10

g1 = Backtracking.Graph(h*w)
g1.graph = GridGraphGen.GridGraphGen(h,w)
path = g1.hamCycle()
print(path)
#generating path
x = np.arange(w)
y = np.arange(h)
z = np.zeros([w,h])
print(z[0])
scale = np.linspace(1, 10, num=len(path))

scaleindex = 0
for node in path:
    row = node // w
    col = node - row*w
    z[col,row] = scale[scaleindex]
    scaleindex += 1

fig, ax = plt.subplots()
ax.pcolor(x,y,z,cmap='RdBu', linewidths=4, shading='auto')
plt.show()


