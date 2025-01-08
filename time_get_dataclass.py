import timeit
import sys
from utils import local_setup, memory_setup, store_results


get_range = """
from zarr.abc.store import ExplicitByteRequest
values = asyncio.run(store.get('c/0', byte_range=ExplicitByteRequest(1,5)))
"""
get_suffix = """
from zarr.abc.store import SuffixByteRequest
values = asyncio.run(store.get('c/0', byte_range=SuffixByteRequest(2)))
"""
get_offset = """
from zarr.abc.store import OffsetByteRequest
values = asyncio.run(store.get('c/0', byte_range=OffsetByteRequest(2)))
"""

func = {
    "get_suffix": get_suffix,
    "get_range": get_range,
    "get_offset": get_offset,
}
setup = {"local": local_setup, "memory": memory_setup}
if __name__ == "__main__":
    method = sys.argv[1]
    storage = sys.argv[2]
    exec_time = timeit.timeit(stmt=func[method], setup=setup[storage], number=10000)
    store_results(__file__, method, storage, exec_time)
