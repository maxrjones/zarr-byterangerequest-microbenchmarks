import timeit
from utils import local_setup, store_results

run = """
values = asyncio.run(store.get('c/0'))
"""

if __name__ == "__main__":
    # timeit statement
    exec_time = timeit.timeit(stmt=run, setup=local_setup, number=10000)
    store_results(__file__, "key", exec_time)
