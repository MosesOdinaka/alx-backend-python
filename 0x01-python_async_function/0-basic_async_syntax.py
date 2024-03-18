#!/usr/bin/env python3
'''
    Description: asynchronous coroutine that takes in an integer argument
    Arguments: max_delay: int = 10.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Return length of delay after waiting up to max_delay seconds '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
