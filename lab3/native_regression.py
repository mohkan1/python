from numpy import *
import sys
import numpy as np
import matplotlib.pyplot as plt


measurements = sys.argv[1]


data = loadtxt(measurements)

dataX = []
dataY = []

print(data)

for row in range(len(data)):
    dataX.append(data[row][0])
    dataY.append(data[row][1])

print(f"{dataX} <<< x")
print(f"{dataY} <<< y")

Xp  = powers(dataX,0,1)
Yp  = powers(dataY,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

print(f"Prediction number of chirps: {[b]} + {[m]} * temperature")

plt.plot(Xp,Yp)
plt.show()





    

