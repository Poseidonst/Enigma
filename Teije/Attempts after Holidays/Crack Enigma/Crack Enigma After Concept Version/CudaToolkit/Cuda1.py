from __future__ import division
from numba import cuda
import numpy
import math
import time

# # CUDA kernel
# @cuda.jit
# def my_kernel(io_array):
#     pos = cuda.grid(1)
#     if pos < io_array.size:
#         io_array[pos] *= 2 # do the computation
#
# # Host code
# data = numpy.ones(256)
# threadsperblock = 256
# blockspergrid = math.ceil(data.shape[0] / threadsperblock)
# my_kernel[blockspergrid, threadsperblock](data)
# print(data)
#
#
# @cuda.jit
# def my_kernel_2D(io_array):
#     x, y = cuda.grid(2)
#     if x < io_array.shape[0] and y < io_array.shape[1]:
#         value = io_array[x][y]
#         value = 10
#         io_array[x][y] = value
#
# data = numpy.full((16, 16), 2)
# threadsperblock = (16, 16)
# blockspergrid_x = math.ceil(data.shape[0] / threadsperblock[0])
# blockspergrid_y = math.ceil(data.shape[1] / threadsperblock[1])
# blockspergrid = (blockspergrid_x, blockspergrid_y)
# my_kernel_2D[blockspergrid, threadsperblock](data)
# print(data)
#
#
#
#
# @cuda.jit
# def my_kernel_3D(io_array):
#     x, y, z = cuda.grid(3)
#     if x < io_array.shape[0] and y < io_array.shape[1] and z < io_array.shape[2]:
#         io_array[x][y][z] *= 2
#
#
# data = numpy.ones((26, 26, 26))
# threadsperblock = (8, 8, 8)
# blockspergrid_x = math.ceil(data.shape[0] / threadsperblock[0])
# blockspergrid_y = math.ceil(data.shape[1] / threadsperblock[1])
# blockspergrid_z = math.ceil(data.shape[2] / threadsperblock[2])
# blockspergrid = (blockspergrid_x, blockspergrid_y, blockspergrid_z)
# my_kernel_3D[blockspergrid, threadsperblock](data)
# print(data)

@cuda.jit
def my_kernel_1D(io_array):
    x, y, z = cuda.grid(3)
    if x < io_array.shape[0] and y < io_array.shape[1] and z < io_array.shape[2]:
        io_array[x][y][z] = x + y + z


data = numpy.ones((26, 26, 26))
threadsperblock = (8, 8, 8)
blockspergrid_x = math.ceil(data.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(data.shape[1] / threadsperblock[1])
blockspergrid_z = math.ceil(data.shape[2] / threadsperblock[2])
blockspergrid = (blockspergrid_x, blockspergrid_y, blockspergrid_z)
my_kernel_1D[blockspergrid, threadsperblock](data)
print(data)
