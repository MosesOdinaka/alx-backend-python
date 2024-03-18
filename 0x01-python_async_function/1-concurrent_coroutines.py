#!/usr/bin/env python3
'''
Description: An async routine called wait_n that takes in 2 int arguments and
             returns the list of all the delay.
Argument: max_delay: int = 10, n: int.
'''

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Returns list of actual delays after waiting for the ran delay. '''
    spawn_ls = []
    delay_ls = []
    for index in range(n):
        taskDelayed = asyncio.create_task(wait_random(max_delay))
        taskDelayed.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(taskDelayed)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
