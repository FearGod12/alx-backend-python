#!/usr/bin/env python3
""" function annotation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float
    by multiplier"""
    def multiplier_func(a: float):
        """multiplies any float"""
        return a * multiplier
    return multiplier_func
