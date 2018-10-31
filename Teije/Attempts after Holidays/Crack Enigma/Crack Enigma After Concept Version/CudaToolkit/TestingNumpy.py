import numpy
import math

data = numpy.ones(256)
for i in range(data.size):
    data[i] *= 2
print(data)
