"""
Helpers.
"""

import tracemalloc
from time import monotonic
from functools import wraps


def time_tracker(f):
    """Print a function running time."""

    @wraps(f)
    def wrap(*args, **kwargs):
        start_time = monotonic()
        result = f(*args, **kwargs)
        end_time = monotonic()
        tracking_time = end_time - start_time

        print(f"{f.__name__}: time tracking: {tracking_time:.8f}")

        return result

    return wrap


def memory_tracker(f):
    """Print a memory usage of function."""

    @wraps(f)
    def wrap(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()

        print(f"{f.__name__}: memory usage: current {current}, peak {peak}")

        tracemalloc.stop()

        return result

    return wrap
