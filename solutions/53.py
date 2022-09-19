from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        for size in range(1, len(nums) + 1):
            for i in range(len(nums) - size + 1):
                print(f"{nums[i : i + size] = }")
                max_sum = max(max_sum, sum(nums[i : i + size]))
        return max_sum


class Solution2:
    """
    Linear Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(cur_sum, max_sum)
        return max_sum


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maxSubArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([5, 4, -1, 7, 8]) == 23
