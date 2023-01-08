from itertools import combinations
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n!)
    Space Complexity: O(1)
    """

    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        for comb in combinations(nums, k):
            ans = min(ans, max(comb) - min(comb))
        return ans


class Solution2:
    """
    Sort and two pointer
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, k - 1
        ans = nums[-1] - nums[0]
        while right < len(nums):
            ans = min(ans, nums[right] - nums[left])
            left += 1
            right += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minimumDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[90], k=1) == 0


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[9, 4, 1, 7], k=2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[20980, 13353, 51423, 11920, 41836, 51586, 54445], k=5) == 33465
