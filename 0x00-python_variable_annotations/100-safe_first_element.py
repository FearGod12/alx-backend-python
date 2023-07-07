#!/usr/bin/env python3
"""duck typing"""
from typing import Sequence, Union, Any, TypeAlias


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns Type Any or None"""
    if lst:
        return lst[0]
    else:
        return None
