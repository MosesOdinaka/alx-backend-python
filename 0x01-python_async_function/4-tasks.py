#!/usr/bin/env python3
'''
Alter a code into a new function.
'''

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Returns sorted list of delay after executing task_wait_random '''
    spawn_ls = []
    delay_ls = []
    for index in range(n):
        taskDelayed = task_wait_random(max_delay)
        taskDelayed.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(taskDelayed)

    for spawn in spawn_ls:
        await spawn
    return delay_ls
