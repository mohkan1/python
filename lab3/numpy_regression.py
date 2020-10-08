from matrix import *
import sys
import numpy as np
import matplotlib.pyplot as plt


measurements = sys.argv[1]
n = sys.argv[2]


data = loadtxt(measurements)

dataX = []
dataY = []

print(data)

for row in range(len(data)):
    dataX.append(data[row][0])
    dataY.append(data[row][1])

print(f"{dataX} <<< x")
print(f"{dataY} <<< y")
"""
Xp  = powers(dataX,0,1)
Yp  = powers(dataY,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

print(f"Prediction number of chirps: {[b]} + {[m]} * temperature")

plt.plot(Xp,Yp)
plt.show()
"""

def powers(data, a, b):
    
    result = []
    result_row = []


    for number in data:
        for ex in range(a, b+1):
            result_row.append(number**ex)
        result.append(result_row)
        result_row = []
    return np.array(result)

    
#Polynomial Regression
Xp  = powers(dataX,0,int(n))
Yp  = powers(dataY,1,1)
Xpt = Xp.transpose()

a = matmul(np.linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]
print(a)

def poly(dataX, a):

    result = []

    for polynom in range(len(dataX)):
        print(dataX[polynom] * a[polynom])
        result.append(dataX[polynom] * a[polynom])
    print(result)
#poly(dataX, a)





    

