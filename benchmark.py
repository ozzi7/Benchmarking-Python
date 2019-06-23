import numpy as np
import timeit
import random


nof_loops = 100
input_size = 1024
input_np = np.float32(np.random.rand(input_size))
input = list()
output_np = np.float32(np.zeros(input_size))
output = list()

for x in range (0, input_size):
    input.append(random.random())
for x in range(0, input_size):
    output.append(0.0)


def decorator(func):
    def wrapper():
        start = timeit.default_timer()
        func()
        stop = timeit.default_timer()
        print("Function {} had {} ops/ms".format(func.__name__, str(int((nof_loops*input_size)/((stop - start)*1000)))))
    return wrapper

def mult_numpy():
    for i in range(nof_loops):
        np.multiply(input_np, 0.5)

def add_numpy():
    for i in range(nof_loops):
        np.add(input_np, 0.5)

def mult():
    for i in range(nof_loops):
        for j in range(input_size):
            input[j]*0.5

decorator(mult)()
decorator(mult_numpy)()
decorator(add_numpy)()