import sys
from datetime import datetime


def store_results(file, method, exec_time):
    with open("timings.csv", "a") as f:
        hatch_env = sys.executable.split("/")[-3]
        f.write(f"{datetime.now()},{file},{hatch_env},{method},{exec_time}\n")


# code snippet to be executed only once
# before the stmt parameter in timeit
local_setup = """
import zarr
import asyncio
store = zarr.storage.LocalStore("example.zarr", read_only=True)
"""

memory_setup = """
import zarr
from zarr.core.buffer import cpu
import asyncio

store = zarr.storage.MemoryStore()
async def set_value(store):
    buffer = cpu.Buffer.from_bytes(b"\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04")
    await store.set("c/0", value=buffer)

asyncio.run(set_value(store))
"""
