import ctypes
from pathlib import Path

dll = ctypes.CDLL("rslib.dll")
dll.rust_function()