"""
recursive function that takes 1 of 2 paths at each char:
take only the current char (1 total),
or take the current and next chars (2 total)

stop when index is out of range or there's a 0

sum all paths in the tree

edge cases: 01

input validation: assume is valid

## challenges found

- for both children of a node the index must be the same
because at any char we can take 1 or 2 chars,
BUT the children of size 2 should start in +1 extra index because we already took 2 chars

- priority of base cases, check if substr size 2 is in dict BEFORE checking remaining equals size

- check for impossible cases and add a way to return 0 at the end of the recursion,
ignoring any actual sum
"""

import pytest


MAX_KEY = 26


def get_possible_ways_rec_original(coded: str) -> int:
    if coded[0] == "0":
        return 0

    is_impossible = False

    def sum_ways(index: int, size: 1 | 2) -> int:
        nonlocal is_impossible
        if is_impossible:
            return -1

        # if substring is not even mapped
        substr = coded[index : index + size]
        if int(substr) > MAX_KEY or substr == "0":
            return 0

        if not is_impossible and substr == "00":
            is_impossible = True
            return -1

        remaining = len(coded) - index
        # when it can take all remaining chars
        if remaining == size:
            return 1

        # when there are not enough chars
        if remaining < size:
            return 0

        return sum_ways(index + size, 1) + sum_ways(index + size, 2)

    size1sum = sum_ways(0, 1)
    size2sum = sum_ways(0, 2)

    if is_impossible:
        return 0

    return size1sum + size2sum


def get_possible_ways_rec_improved(coded: str) -> int:
    if coded == "01":
        return 0

    def sum_ways(index: int = 0) -> int:
        """
        time O(2**n)
        space O(n)
        """
        # if end of string is reached, this path is a valid decoding
        if index == len(coded):
            return 1

        # if current char is 0, this path is invalid
        if coded[index] == "0":
            return 0

        # sum paths of taking this single char
        ways = sum_ways(index + 1)

        # if current char is last
        if index + 1 >= len(coded):
            # can't take 2-digit substring
            return ways

        substr = coded[index : index + 2]
        # if 2-digit substring is not even mapped
        if int(substr) > MAX_KEY:
            return ways

        # sum paths of taking this and next chars
        ways += sum_ways(index + 2)

        return ways

    # O(2**n)
    return sum_ways()


def get_possible_ways_mem_improved(coded: str) -> int:
    if coded == "01":
        return 0

    # O(n)
    memory = [None for _ in range(len(coded))]

    def sum_ways(index: int = 0) -> int:
        """
        time O(n)
        space O(n)
        """
        # if end of string is reached, this path is a valid decoding
        if index == len(coded):
            return 1

        # if current char is 0, this path is invalid
        if coded[index] == "0":
            return 0

        # if solution for current index was already found
        if memory[index] is not None:
            return memory[index]

        # sum paths of taking this single char
        ways = sum_ways(index + 1)

        # if current char is last
        if index + 1 >= len(coded):
            # can't take 2-digit substring
            return ways

        substr = coded[index : index + 2]
        # if 2-digit substring is not even mapped
        if int(substr) > MAX_KEY:
            return ways

        # sum paths of taking this and next chars
        ways += sum_ways(index + 2)

        # save solution for this index
        memory[index] = ways

        return ways

    # O(n)
    return sum_ways()


@pytest.mark.parametrize(
    "coded,expected_ways",
    [
        ("01", 0),
        ("12", 2),
        ("10", 1),
        ("100", 0),
        ("123", 3),
        ("1234", 3),
        ("12345", 3),
        ("123456", 3),
        ("12003", 0),
        ("226", 3),
        ("06", 0),
        ("111", 3),  # aaa, ak, ka
        ("1111", 5),
        ("2222", 5),
        ("7" * 100, 1),
        ("0", 0),
    ],
)
def test(coded: str, expected_ways: int):
    assert expected_ways == get_possible_ways_rec_original(coded)
    assert expected_ways == get_possible_ways_rec_improved(coded)
    assert expected_ways == get_possible_ways_mem_improved(coded)
