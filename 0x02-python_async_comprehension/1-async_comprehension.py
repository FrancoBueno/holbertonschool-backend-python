#!/usr/bin/env python3
""" Py asinc func """

from typing import List
async_generator = __import__('0-async_generator').async_generator
Vector = List[float]


async def async_comprehension -> Vector:
    """ return async func """
    tareal = [i async for i in async_generator()]
    return tareal
