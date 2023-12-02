import ctypes

# import matplotlib.image as img
import numpy as np

clibrary = ctypes.CDLL(r"C:/Users/ASUS/Desktop/project/project_present/hellotest.so")

c = [int(1),int(2),int(3)]
b = clibrary.display(id(c))
print(b)
