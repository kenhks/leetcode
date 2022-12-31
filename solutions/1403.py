from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort by descending
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + 2n
    Space Complexity: O(1)
    """

    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        cutoff = sum(nums) / 2
        c_total = 0
        ans = []
        for i in range(len(nums)):
            c_total += nums[i]
            ans.append(nums[i])
            if c_total > cutoff:
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minSubsequence",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[4, 3, 10, 9, 8]) == [10, 9]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[4, 4, 7, 6, 7]) == [7, 7, 6]
