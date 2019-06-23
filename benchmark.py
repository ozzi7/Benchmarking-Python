import numpy as np
import timeit

nof_loops = 10000
input_size = 1024
input = np.random.rand(input_size)
output = np.zeros(input_size)

def decorator(func):
    def wrapper():
        start = timeit.default_timer()
        func()
        stop = timeit.default_timer()
        print("Function {} had {} ops/ms".format(func.__name__, str(int((nof_loops*input_size)/((stop - start)*1000)))))
    return wrapper

def mult_numpy():
    for i in range(nof_loops):
        np.multiply(input,0.5)

def mult():
    for i in range(nof_loops):
        for j in range(input_size):
            output[j] = input[j]*0.5

decorator(mult)()
decorator(mult_numpy)()