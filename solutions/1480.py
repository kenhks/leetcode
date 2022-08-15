from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Inplace
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "runningSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3, 4]) == [1, 3, 6, 10]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
