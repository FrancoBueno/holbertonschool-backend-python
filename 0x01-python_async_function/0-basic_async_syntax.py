#!/usr/bin/env python3
"""Comentario pa agregar"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """take in the argument , the delay and return the delay"""
    randon = random.uniform(0, max_delay)
    await asyncio.sleep(randon)
    return randon
