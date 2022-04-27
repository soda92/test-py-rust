import ctypes

dll = ctypes.CDLL("./target/debug/rslib.dll")
dll.rust_function()
