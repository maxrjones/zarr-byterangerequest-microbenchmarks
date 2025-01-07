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
store = store = zarr.storage.LocalStore("example.zarr", read_only=True)
"""
