"""
minimize amount of potholes to go over
assuming a car can not travel diagonally

heuristic of avoiding immediate pothole
won't work,
we need to check all possible paths
and choose the one with the minimum amount of potholes

dynamic programming?
from any segment, there are only 2 possible options
so decision tree is a binary tree
if this approach returns path with min pots,
    count total pots then subtract answer

in a recursive function,
carry sum of pots and return min?

how to memoize?

I think I got stuck with avoiding circular references,
and how to accurately carry the sum of pots so far

-------------------------------------------------------

the trick is that once a car switched lanes, it should just avoid going back i.e. switch lanes again
going right must always be explored, but switching lanes should only be done once, then continue right
in the binary tree this also looks like a zig-zag
"""


def solve(l1: list[str], l2: list[str]) -> int:
    """
    time O(2**n)

    space O(n)
    """
    POTHOLE = "x"

    L1 = 1
    L2 = -1

    def dfs(lane: int, i=0, currsum=0, parent_id: tuple[int, int] = (0, -1)):
        if i >= len(l1):
            return currsum

        road = l1 if lane == L1 else l2
        pot = 1 if road[i] == POTHOLE else 0
        newsum = currsum + pot

        curr_id = (lane, i)

        go_right = dfs(lane, i + 1, newsum, curr_id)

        # if last step switched lane
        if (-lane, i) == parent_id:
            # avoid going back by switching lane again
            return go_right

        switch_lane = dfs(-lane, i, newsum, curr_id)
        return min(go_right, switch_lane)

    # O(2**n)? O(n**2)?
    minpath = min(dfs(L1), dfs(L2))

    # O(n)
    total = sum(1 for l in l1 + l2 if l == POTHOLE)

    # count total, subtract
    return total - minpath


import pytest


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ("..xx.x.", "x.x.x..", 4),
        (".xxx...x", "..x.xxxx", 6),
        ("xxxxx", ".x..x", 5),
        ("x...x", "..x..", 3),
    ],
)
def test_solution(l1, l2, expected):
    assert solve(l1, l2) == expected
