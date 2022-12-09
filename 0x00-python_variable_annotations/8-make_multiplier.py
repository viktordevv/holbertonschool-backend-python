#!/usr/bin/env python3
""" Takes a float multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and returns a float"""
    return (lambda x: multiplier*x)
