from random import randint
import matplotlib.pyplot as plt
plt.switch_backend('agg')

fig, ax = plt.subplots(figsize=(10, 8))
points = list()
last = 0
bound = 100
for i in range(0, 100):
  last += randint(-bound, bound)
  points.append(last)

ax.plot(points)
fig.savefig('graph.png')
