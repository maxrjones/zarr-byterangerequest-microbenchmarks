import timeit
import sys
from utils import local_setup, store_results


get_range = """
from zarr.abc.store import ExplicitRange
values = asyncio.run(store.get('c/0', byte_range=ExplicitRange(1,5)))
"""
get_suffix = """
from zarr.abc.store import SuffixRange
values = asyncio.run(store.get('c/0', byte_range=SuffixRange(2)))
"""
get_offset = """
from zarr.abc.store import OffsetRange
values = asyncio.run(store.get('c/0', byte_range=OffsetRange(2)))
"""

func = {
    "get_suffix": get_suffix,
    "get_range": get_range,
    "get_offset": get_offset,
}
if __name__ == "__main__":
    method = sys.argv[1]
    exec_time = timeit.timeit(stmt=func[method], setup=local_setup, number=10000)
    store_results(__file__, method, exec_time)
