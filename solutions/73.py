from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Modify in-place with column_set
    Binary Search
    Time Complexity: O(mn) = 2mn
    Space Complexity: O(m + n)
    m = the number of rows
    n = the number of columns
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix[0]), len(matrix)
        col_set = set()
        row_set = set()
        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    col_set.add(x)
                    row_set.add(y)
        for col in col_set:
            for y in range(n):
                matrix[y][col] = 0
        for row in row_set:
            for x in range(m):
                matrix[row][x] = 0


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "setZeroes",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    expected = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    solution(matrix)
    assert matrix == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    expected = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
    solution(matrix)
    assert matrix == expected
