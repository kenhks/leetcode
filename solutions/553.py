from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            ans = str(nums[0])
        elif len(nums) == 2:
            ans = "/".join(map(str, nums))
        else:
            ans = "{}/({})".format(nums[0], "/".join(map(str, nums[1:])))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "optimalDivision",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1000, 100, 10, 2]) == "1000/(100/10/2)"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[2, 3, 4]) == "2/(3/4)"
