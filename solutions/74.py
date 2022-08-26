from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary Search
    Time Complexity: O(log(2, m + n))
    Space Complexity: O(1)
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_left, y_right = 0, len(matrix) - 1
        while y_left <= y_right:
            y_mid = (y_left + y_right) // 2
            if matrix[y_mid][0] == target:
                return True
            elif matrix[y_mid][0] > target:
                y_right = y_mid - 1
            elif matrix[y_mid][-1] < target:
                y_left = y_mid + 1
            else:
                x_left, x_right = 1, len(matrix[0]) - 1
                while x_left <= x_right:
                    x_mid = (x_left + x_right) // 2
                    if matrix[y_mid][x_mid] == target:
                        return True
                    elif matrix[y_mid][x_mid] > target:
                        x_right = x_mid - 1
                    else:
                        x_left = x_mid + 1
                break
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "searchMatrix",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert solution(matrix, 3)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert not solution(matrix, 13)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert solution(matrix, 30)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert not solution(matrix, 70)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    matrix = [
        [1, 3, 5],
    ]
    assert solution(matrix, 5)


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    matrix = [
        [1, 3, 5],
    ]
    assert not solution(matrix, 2)
