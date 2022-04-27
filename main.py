import ctypes

dll = ctypes.CDLL("./rslib.dll")
dll.rust_function()
