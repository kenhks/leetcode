from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan start from bottom left to top right
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    m = the number of rows
    n = the number of columns
    """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ans = True
        for y in range(len(matrix) - 1, -1, -1):
            next_y, next_x, value = y + 1, 1, matrix[y][0]
            while next_y < len(matrix) and next_x < len(matrix[0]):
                if value != matrix[next_y][next_x]:
                    ans = False
                    break
                next_x += 1
                next_y += 1
            if not ans:
                break
        for x in range(1, len(matrix[0])):
            next_y, next_x, value = 1, x + 1, matrix[0][x]
            while next_y < len(matrix) and next_x < len(matrix[0]):
                if value != matrix[next_y][next_x]:
                    ans = False
                    break
                next_x += 1
                next_y += 1
            if not ans:
                break
        return ans


class Solution2:
    """
    Element-wise Scan
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    m = the number of rows
    n = the number of columns
    """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[row + 1][1:] == matrix[row][:-1] for row in range(len(matrix) - 1))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isToeplitzMatrix",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2],
    ]
    assert solution(matrix)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 2],
        [2, 2],
    ]
    assert not solution(matrix)
