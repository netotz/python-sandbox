"""
The Validator checks that a solution of peaks and valleys is valid for some array.
"""

from models import PeakOrValley
from generator import is_peak_or_valley


def is_valid_solution(numbers: list[int], pvs: list[PeakOrValley]) -> bool:
    # O(n)
    for pv in pvs:
        if not is_peak_or_valley(numbers, pv.index):
            return False

    return True
