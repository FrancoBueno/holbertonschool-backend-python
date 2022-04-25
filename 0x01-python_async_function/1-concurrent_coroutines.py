#!/usr/bin/env python3
""" Function"""

import asyncio
import random

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for wait_random a lot of times """
    tsk = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(tsk)]
    return delay
