"""
Generator of instances.
"""

import math
from random import Random

from models import Instance, PeakOrValley


def generate(size: int, seed: int | None) -> Instance:
    """
    Generates an instance of size `size`.

    Constraints:
        = `size > 0`
        - `-n < A[0] < n` where `n == size` and `A` the array of peaks and valleys
        - `A[i] = A[i - 1] +|- 1`
        - `A[-1] = A[n] = -inf`
    """
    if size <= 0:
        raise ValueError("size must be > 0")

    rnd = Random(seed)

    first = rnd.randint(-size + 1, size - 1)
    numbers = [first]

    pvs: list[PeakOrValley] = []

    # O(n)
    for i in range(1, size):
        is_positive = rnd.random() >= 0.5
        factor = 1 if is_positive else -1
        unit = factor * 1

        newnum = numbers[i - 1] + unit
        numbers.append(newnum)

        if is_peak_or_valley(numbers, i - 1):
            pv = PeakOrValley(numbers[i - 1], i - 1)
            pvs.append(pv)

    last_index = size - 1

    # check last number
    if is_peak_or_valley(numbers, last_index):
        pv = PeakOrValley(numbers[-1], last_index)
        pvs.append(pv)

    instance = Instance(numbers, pvs)

    return instance


def is_peak_or_valley(numbers: list[int], index: int):
    # neighbors, indices could be out of range
    left = -math.inf if index == 0 else numbers[index - 1]
    right = -math.inf if index == len(numbers) - 1 else numbers[index + 1]

    return (
        # is valley
        left > numbers[index] < right
        # or peak
        or left < numbers[index] > right
    )
