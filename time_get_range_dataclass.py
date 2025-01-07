import timeit
from utils import local_setup, store_results


run = """
from zarr.abc.store import ExplicitRange
values = asyncio.run(store.get('c/0', byte_range=ExplicitRange(1,5)))
"""


if __name__ == "__main__":
    exec_time = timeit.timeit(stmt=run, setup=local_setup, number=10000)
    store_results(__file__, "range", exec_time)
