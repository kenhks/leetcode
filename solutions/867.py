from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math swap x,y
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix[0]), len(matrix)
        matrix_T = []
        for y in range(m):
            matrix_T.append([matrix[i][y] for i in range(n)])
        return matrix_T


class Solution2:
    """
    Pythonic
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "transpose",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert solution(matrix) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert solution(matrix) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]
