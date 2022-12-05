from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DP Top down, Iterative
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(1, len(triangle)):
            triangle[level][0] += triangle[level - 1][0]
            triangle[level][-1] += triangle[level - 1][-1]
            for i in range(1, level):
                triangle[level][i] += min(triangle[level - 1][i - 1], triangle[level - 1][i])
        return min(triangle[-1])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minimumTotal",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    assert solution(triangle) == 11


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    triangle = [[-10]]
    assert solution(triangle) == -10
