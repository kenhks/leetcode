from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + 2n
    Space Complexity: O(n)
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_map = defaultdict(int)
        prev = None
        for i, n in enumerate(sorted(nums)):
            if i == 0:
                count_map[n] = 0
            elif n > prev:
                count_map[n] = i
            prev = n
        return [count_map[n] for n in nums]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "smallerNumbersThanCurrent",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[6, 5, 4, 8]) == [2, 1, 0, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[7, 7, 7, 7]) == [0, 0, 0, 0]
