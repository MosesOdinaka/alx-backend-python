#!/usr/bin/env python3
'''
A coroutine called async_comprehension, and collect 10 numbers
using an async comprehension, then return the 10 random numbers.
'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' The value yielded by th async_generator is return. '''
    return [value async for value in async_generator()]
