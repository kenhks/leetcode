from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    4 pointer swap
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for level in range(size // 2):
            x_upper = y_upper = size - 1 - level
            x_lower = y_lower = level
            for x in range(x_lower, x_upper):
                shift = x - y_lower
                (
                    matrix[y_lower + shift][y_upper],
                    matrix[y_upper][x_upper - shift],
                    matrix[y_upper - shift][x_lower],
                    matrix[y_lower][x],
                ) = (
                    matrix[y_lower][x],
                    matrix[y_lower + shift][y_upper],
                    matrix[y_upper][x_upper - shift],
                    matrix[y_upper - shift][x_lower],
                )


class Solution2:
    """
    Math, Transpose & Vertical Flip
    Time Complexity: O(2n^2)
    Space Complexity: O(1)
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for y in range(size):
            for x in range(size):
                if x < y:
                    matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        for y in range(size):
            matrix[y] = matrix[y][::-1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "rotate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    solution(matrix)
    assert matrix == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    solution(matrix)
    assert matrix == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]
