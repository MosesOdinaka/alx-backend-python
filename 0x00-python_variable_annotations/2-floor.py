#!/usr/bin/env python3
'''
    Description: Return the floor of a float n argurment.
    Parameter: n: float.
'''


def floor(n: float) -> int:
    ''' Return the largest integer value that is <= to n. '''
    return int(n) if n >= 0 else int(n) - 1;
