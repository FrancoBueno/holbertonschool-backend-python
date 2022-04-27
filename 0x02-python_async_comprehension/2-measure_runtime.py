#!/usr/bin/env python3
"""Py async func"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ret time """
    stime = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    etime = time.perf_counter()
    return etime - stime
