from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with minimum absolute value
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        abs_ans = abs(nums[0])
        for n in nums[1:]:
            abs_n = abs(n)
            if abs_n == abs_ans:
                ans = max(n, ans)
            elif abs_n < abs_ans:
                ans, abs_ans = n, abs_n
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findClosestNumber",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-4, -2, 1, 4, 8]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([2, -1, 1]) == 1
