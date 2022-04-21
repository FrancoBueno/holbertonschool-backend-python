#!/usr/bin/env python3
""" python return value type"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element lenght """
    return [(i, len(i)) for i in lst]
