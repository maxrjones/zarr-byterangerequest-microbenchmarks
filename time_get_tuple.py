import timeit
import sys
from utils import local_setup, store_results

get_range = """
values = asyncio.run(store.get('c/0', byte_range=(1, 4)))
"""
get_suffix = """
values = asyncio.run(store.get('c/0', byte_range=(-2, None)))
"""
get_offset = """
values = asyncio.run(store.get('c/0', byte_range=(2, None)))
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
