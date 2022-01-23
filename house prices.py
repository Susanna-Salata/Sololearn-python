import numpy as np


data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

sel = data[(data >= np.mean(data)-np.std(data))&(data <= np.mean(data)+np.std(data))]

print((len(sel)/len(data))*100)
