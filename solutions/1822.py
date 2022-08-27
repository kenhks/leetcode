from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Linear Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for i in nums:
            if i == 0:
                sign = 0
                break
            elif i < 0:
                sign = -sign
        return sign


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "arraySign",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-1, -2, -3, -4, 3, 2, 1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 5, 0, 2, -3]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([-1, 1, -1, 1, -1]) == -1
