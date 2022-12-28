from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sorted Remaining Capacity
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = [i - j for i, j in zip(capacity, rocks)]
        diffs.sort()
        ans = 0
        for d in diffs:
            if d == 0:
                ans += 1
            elif additionalRocks >= d:
                additionalRocks -= d
                ans += 1
            else:
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumBags",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2
    assert solution(capacity, rocks, additionalRocks) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    capacity = [10, 2, 2]
    rocks = [2, 2, 0]
    additionalRocks = 100
    assert solution(capacity, rocks, additionalRocks) == 3
