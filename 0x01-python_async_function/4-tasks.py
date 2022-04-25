#!/usr/bin/env python3
""" function 4 asdasdas"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task wait_n task 4 dalee dale"""
    tsk = [task_wait_random(max_delay) for _ in range(n)]
    dly = [await task for task in asyncio.as_completed(tsk)]
    return dly
