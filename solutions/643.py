from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k]) / k
        for i in range(1, len(nums) - k + 1):
            ans = max(ans, sum(nums[i : i + k]) / k)
        return ans


class Solution2:
    """
    Rolling Sum
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = c_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            c_sum += nums[i] - nums[i - k]
            max_sum = max(c_sum, max_sum)
        return max_sum / k


class Solution3:
    """
    Cumulative Sum
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cum_sum = [0] * len(nums)
        for i, n in enumerate(nums):
            cum_sum[i] = cum_sum[i - 1] + n
        max_sum = cum_sum[k - 1]
        for i in range(k, len(nums)):
            max_sum = max(max_sum, cum_sum[i] - cum_sum[i - k])
        return max_sum / k


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "findMaxAverage",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[5], k=1) == 5


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[-1, 0, 1], k=1) == 1
