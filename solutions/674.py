from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c_len, max_len = 1, 1
        prev_n = nums[0]
        for n in nums[1:]:
            if n > prev_n:
                c_len += 1
                max_len = max(c_len, max_len)
            else:
                c_len = 1
            prev_n = n
        return max_len


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findLengthOfLCIS",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 3, 5, 4, 7]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[2, 2, 2, 2, 2]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[1]) == 1
