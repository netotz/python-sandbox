from dataclasses import dataclass


@dataclass
class PeakOrValley:
    number: int
    index: int


@dataclass
class Instance:
    array: list[int]
    pvs: list[PeakOrValley]
    """
    List of peaks and valleys.
    """
