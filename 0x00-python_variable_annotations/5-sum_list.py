#!/usr/bin/env python
'''
    Descriptin: A type annotated function  which takes a list of floats as
        argument.
    Parameter: input_list: list[float]
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Return sum of elements in input_list. '''
    return sum(input_list)
