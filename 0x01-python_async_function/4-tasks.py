#!/usr/bin/env python3
"""Spawn wait_random n times with the specified max_delay"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with the specified max_delay"""
    res = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))

    # Sort result in ascending order
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]

    return res
