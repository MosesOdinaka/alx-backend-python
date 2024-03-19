#!/usr/bin/env python3
'''
Coroutine that collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Execute async_comprehension four times in the parallel '''
    Time_1 = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    Time_2 = time()

    return Time_2 - Time_1
