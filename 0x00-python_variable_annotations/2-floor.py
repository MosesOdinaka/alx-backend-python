#!/usr/bin/env python3
'''
    Description: Return the floor of a float n argument.
    Parameter: n: float.
'''


def floor(n: float) -> int:
    ''' Return the largest integer value that is <= to n. '''
    return n if n >= 0 else n - 1;
