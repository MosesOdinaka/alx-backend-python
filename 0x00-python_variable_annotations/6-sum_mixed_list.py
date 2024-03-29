#!/usr/bin/env python3
'''
    Description: A  type-annotated function sum_mixed_list which takes a list
                mxd_lst of integers and floats and returns their sum
                as a float.
    Parameter: mxd_lst: List[union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Output the sum of the elements of mxd_lst. '''
    return sum(mxd_lst)
