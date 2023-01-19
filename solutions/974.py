from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Rolling Sum
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            arr_sum = 0
            for j in range(i, len(nums)):
                arr_sum += nums[j]
                if arr_sum % k == 0:
                    ans += 1
        return ans


class Solution2:
    """
    DP, Hashmap of sum
    Time Complexity: O(n)
    Space Complexity: O(k)
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prev_sum = {0: 1}
        c_sum = 0
        for n in nums:
            c_sum = (c_sum + n) % k
            ans += prev_sum.get(c_sum, 0)
            prev_sum[c_sum] = prev_sum.get(c_sum, 0) + 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "subarraysDivByK",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    assert solution(nums, k) == 7


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [5]
    k = 9
    assert solution(nums, k) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1, 10, 100, 1000, 10000, 100000]
    k = 3
    assert solution(nums, k) == 5
