import zarr
from zarr.core.buffer import cpu
import asyncio


async def set_value():
    buffer = cpu.Buffer.from_bytes(b"\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04")
    store = zarr.storage.LocalStore("example.zarr", read_only=False)
    await store.set("c/0", value=buffer)


asyncio.run(set_value())
