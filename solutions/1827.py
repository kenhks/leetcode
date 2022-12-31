from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                ans += prev - nums[i]
            else:
                prev = nums[i]
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minOperations",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 1, 1]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 5, 2, 4, 1]) == 14


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[8]) == 0
