from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    hashset
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for n in nums:
            seen.add(n)
            if -n in seen:
                ans = max(abs(n), ans)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findMaxK",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-1, 2, -3, 3]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([-1, 10, 6, 7, -7, 1]) == 7


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([-10, 8, 6, 7, -2, -3]) == -1
