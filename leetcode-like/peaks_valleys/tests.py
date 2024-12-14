import pytest

from generator import generate, is_peak_or_valley
from models import Instance, PeakOrValley


@pytest.mark.parametrize(
    "array, index, is_it",
    [
        ([0], 0, True),  # peak
        ([-999999999], 0, True),  # still a peak
        ([0, 1, 0], 1, True),  # peak
        ([1, 0], 0, True),  # peak
        ([0, 1], 1, True),  # peak
        ([0, -1, 0], 1, True),  # valley
        ([-1, 0], 0, False),
        ([0, -1], 1, False),
    ],
)
def test_is_peak_or_valley(array: list[int], index: int, is_it: bool) -> None:
    actual = is_peak_or_valley(array, index)

    assert actual == is_it


SEED = 20241214


@pytest.mark.parametrize(
    "numbers, pvs",
    [
        ([0], [PeakOrValley(0, 0)]),
        ([0, 1, 0], [PeakOrValley(1, 1)]),
        ([1, 0], [PeakOrValley(1, 0)]),
        ([0, 1], [PeakOrValley(1, 1)]),
        ([0, -1, 0], [PeakOrValley(-1, 1)]),
        ([-1, 0], [PeakOrValley(0, 1)]),
        ([0, -1], [PeakOrValley(0, 0)]),
        (
            [2, 3, 4, 5, 6, 5, 4, 5, 4],
            [
                PeakOrValley(6, 4),
                PeakOrValley(4, 6),
                PeakOrValley(5, 7),
            ],
        ),
        (
            [1, 2, 3, 1],
            [
                PeakOrValley(3, 2),
            ],
        ),
        (
            [1, 2, 1, 2, 3, 4, 3],
            [
                PeakOrValley(2, 1),
                PeakOrValley(1, 2),
                PeakOrValley(4, 5),
            ],
        ),
    ],
)
def test_is_valid_solution(numbers: list[int], pvs: list[PeakOrValley]) -> None:
    # O(n)
    for pv in pvs:
        assert is_peak_or_valley(numbers, pv.index)
