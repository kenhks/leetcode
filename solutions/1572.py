from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0 if n % 2 == 0 else -mat[n // 2][n // 2]
        for y in range(n):
            ans += mat[y][y] + mat[y][n - 1 - y]
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "diagonalSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert solution(mat) == 25


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    mat = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]
    assert solution(mat) == 8
