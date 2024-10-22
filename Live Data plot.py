import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections
import FOPTD_final

cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
print("CPU: {}".format(cpu))
print("Memory: {}".format(ram))
# function to update the data
def my_function(i):
    # get data
    temp_ip = FOPTD_final.xs[i]
    temp_op = FOPTD_final.ys[i]
    cpu.popleft()
    cpu.append(temp_ip)
    ram.popleft()
    ram.append(temp_op)
    # clear axis
    ax.cla()
    
    # plot cpu
    ax.plot(cpu)
    ax.scatter(len(cpu)-1, cpu[-1])
    
    # plot memory
    ax.plot(ram)
    ax.scatter(len(ram)-1, ram[-1])
  
# start collections with zeros
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure()
ax = plt.subplot(111)
ax.set_facecolor('#DEDEDE')

# animate
ani = FuncAnimation(fig, my_function, interval=1000)
plt.show()
