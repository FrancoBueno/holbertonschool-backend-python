#!/usr/bin/env python3
""" Py asinc func"""

import asyncio
from typing import Generator
import random


async def function async_generator() -> Generator[float, None, None]:
    """return the list"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
