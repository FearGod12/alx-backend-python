#!/usr/bin/env python3
"""function annotation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple of sequence"""
    return [(i, len(i)) for i in lst]
