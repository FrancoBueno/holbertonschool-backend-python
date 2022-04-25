#!/usr/bin/env python3
"""  Func """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns time total"""
    inicio = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    tiempototal = time.perf_counter() - inicio
    return tiempototal / n
