#!/usr/bin/env python3
"""measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the time take to execute async_comprehension
    four times using asyncio.gather"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
