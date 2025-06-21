# # 1. Crear una lista con números que comiencen por 30 y que termine en 42 haciendo que el paso entre cada número consecutivo sea de 0.4. Sin usar Numpy.

# def frange(init = 0, end = 1, step = 0.1):
#     numbers = []

#     while init <= end or math.isclose(init,2):
#         numbers.append(round(init, 2))
#         init += step
#     return numbers

# print(frange(30,42,0.4))



import math

def frange(init = 0, end = 1, step = 0.1) : 
    numbers = []

    while init < end or math.isclose(init, end):
        numbers. append(round(init,2))
        init += step
    return numbers

print(frange(30,42,0.4))


# import numpy as np

# mi_lista=np.arange(30, 42, 0.4)

# print(mi_lista)
