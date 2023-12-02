import ctypes

clibrary = ctypes.CDLL(r"C:/Users/ASUS/Desktop/project/project_present/hellotest.so")

clibrary.display(2)