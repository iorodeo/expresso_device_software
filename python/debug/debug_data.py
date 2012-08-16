import matplotlib
matplotlib.use('GtkAgg')
import pylab
import numpy as np
import sys
import time

with open('debug_data.txt','r') as f:
    lines = f.readlines()
upper = []
lower = []
t_sec = []
level = []
for line in lines:
    data_list = line.split(' ')
    t = time.strptime(data_list[1],'%H:%M:%S')
    t = time.mktime(t)
    t_sec.append(t)
    level.append(float(data_list[2]))
    lower.append((int(data_list[3]),int(data_list[4])))
    upper.append((int(data_list[5]),int(data_list[6]))) 

lower = np.array(lower)
upper = np.array(upper)
level = np.array(level)
t_sec = np.array(t_sec)

mid_point = np.mean(np.array([lower[:,0],upper[:,0]]),axis=0)

#pylab.plot(t_sec-t_sec[0],level,'r.')
pylab.plot(t_sec-t_sec[0],mid_point,'b.')
ax = pylab.gca()
ax.set_ylim([190,220])

pylab.xlabel('time (s)')
pylab.grid(True)
pylab.show()
