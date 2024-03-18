#!/usr/bin/env python3
'''
Measures the total execution time, and returns total_time / n.
'''

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' The execution time is return for wait_n '''
    time_00 = time()
    run(wait_n(n, max_delay))
    time_01 = time()
    timeElapsed = time_01 - time_00
    return timeElapsed / n
