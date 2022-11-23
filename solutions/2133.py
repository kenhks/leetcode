from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset count
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    n = len(matrix)
    """

    def checkValid(self, matrix: List[List[int]]) -> bool:
        ans = True
        for row in matrix:
            if len(set(row)) != len(matrix):
                ans = False
                break
        for col in zip(*matrix):
            if len(set(col)) != len(matrix):
                ans = False
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkValid",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1],
    ]
    assert solution(matrix)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 1, 1],
        [1, 2, 3],
        [1, 2, 3],
    ]
    assert not solution(matrix)
