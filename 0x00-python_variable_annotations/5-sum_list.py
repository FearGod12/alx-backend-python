#!/usr/bin/env python3
"""type-annotated function sum_list"""


def sum_list(input_list: list[float]) -> float:
    """takes a list input_list of floats as argument and returns their sum as a float."""
    return sum(input_list)
