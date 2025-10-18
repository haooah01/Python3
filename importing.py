"""Demonstrates importing modules and functions from external libraries."""

import random
from time import perf_counter as clock  # clock is deprecated; use perf_counter instead.

randomint = random.randint(1, 100)

if __name__ == "__main__":
    print(randomint)
    print(clock())
