from ctypes import *

if __name__ == '__main__':
    '''/ICESX/workSpaceC/PythonWithC/Debug/libPythonWithC.so'''
    sofile = "/ICESX/workSpaceC/PythonWithC/Debug/libPythonWithC.so"
    libtest = cdll.LoadLibrary(sofile)
    print(libtest.ivoke(2))
    print(libtest.ivoke(2,3))
