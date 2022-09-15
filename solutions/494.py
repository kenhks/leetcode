from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def sum_array(next_index, c_sum):
            nonlocal count
            if next_index == len(nums):
                if c_sum == target:
                    count += 1
            else:
                sum_array(next_index + 1, c_sum + nums[next_index])
                sum_array(next_index + 1, c_sum - nums[next_index])

        sum_array(0, 0)
        return count


class Solution2:
    """
    DP with cumsum hashmap
    Time Complexity: O(2^n) = 2^(n+2) - 2
    Space Complexity: O(2^n)
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cumsum = {0: 1}
        for i in nums:
            new_cumsum = {}
            for s in cumsum:
                if i == 0:
                    new_cumsum[s] = cumsum[s] * 2
                else:
                    for new_sum in (s + i, s - i):
                        if new_sum not in new_cumsum:
                            new_cumsum[new_sum] = cumsum[s]
                        else:
                            new_cumsum[new_sum] += cumsum[s]
            cumsum = new_cumsum
        return cumsum[target] if target in cumsum else 0


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findTargetSumWays",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 1, 1, 1, 1], target=3) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1], target=1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([10], target=5) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([0, 0, 0, 0, 0, 0, 0, 0, 1], target=1) == 256
