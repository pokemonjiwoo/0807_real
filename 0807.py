import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random.uniform(0,100) for _ in range(100)]
y = [2 * val + 1 +random.uniform(-10, 10) for val in x]
plt.clf()
#data of line
x_line = range(101)
y_line = [2 * val + 1 for val in x_line]

plt.scatter(x, y, label = "Random Data Points", color = "green", marker = "o", s = 30, alpha = 0.5)
#line plot
plt.plot(x_line, y_line, label = 'y = 2x = 1', color = 'red')
plt.title('Scatter plot example')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.savefig("./scatter.png")
plt.show()




