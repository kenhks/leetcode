from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for s in range(len(nums) + 1, 0, -1):
            for i in range(len(nums) - s + 1):
                if sum(nums[i : i + s]) == k:
                    ans += 1
        return ans


class Solution2:
    """
    Cumulative sum
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                if total == k:
                    ans += 1
        return ans


class Solution3:
    """
    Hashmap, the count of cumulative sum
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        cumsum_map = {0: 1}
        for n in nums:
            total += n
            prev_total = total - k
            if prev_total in cumsum_map:
                ans += cumsum_map[prev_total]
            cumsum_map[total] = cumsum_map.get(total, 0) + 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "subarraySum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 1, 1], k=2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 2, 3], k=3) == 2
