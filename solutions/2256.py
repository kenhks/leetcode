from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = 0
        min_avg_diff = 10**5
        for i in range(1, len(nums) + 1):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i:])
            if right_sum == 0:
                right_avg = 0
            else:
                right_avg = right_sum // (len(nums) - i)
            avg_diff = abs(left_sum // i - right_avg)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                ans = i - 1
        return ans


class Solution2:
    """
    Rolling Sum
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = len(nums) - 1
        left_sum, right_sum = sum(nums), 0
        if left_sum == 0:
            return 0
        min_avg_diff = left_sum / len(nums)
        for i in range(len(nums) - 1, 0, -1):
            left_sum -= nums[i]
            right_sum += nums[i]
            avg_diff = abs(left_sum // i - right_sum // (len(nums) - i))
            if avg_diff <= min_avg_diff:
                min_avg_diff = avg_diff
                ans = i - 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minimumAverageDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 5, 3, 9, 5, 3]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([0, 0, 0, 0, 0]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([0, 0, 3]) == 0
