import ctypes
from pathlib import Path

CURRENT = Path(__file__).resolve().parent
target = CURRENT.joinpath("target/debug/rslib.dll")

dll = ctypes.CDLL(str(target))
dll.rust_function()
