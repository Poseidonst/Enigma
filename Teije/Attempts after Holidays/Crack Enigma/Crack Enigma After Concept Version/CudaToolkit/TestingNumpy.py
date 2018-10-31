import numpy
import math

data = numpy.ones(256)
for i in range(data.size):
    data[i] *= 2

data2 = numpy.ones((16, 16))
for i in range(16):
    for j in range(16):
        data2[i][j] *= 2
print(data)
print(data2)

data3 = numpy.empty((2, 2), dtype=int)
print(data3)
