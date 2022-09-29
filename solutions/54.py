from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Follow the spiral order with min-max value
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix[0]), len(matrix)
        total = m * n
        res = [None] * total
        count = 0
        x = y = 0
        direction = 0
        x_min, y_min = 0, 1
        x_max, y_max = m - 1, n - 1
        while count < total:
            res[count] = matrix[y][x]
            if direction == 0:
                if x == x_max:
                    direction = 1
                    x_max -= 1
                    y += 1
                else:
                    x += 1
            elif direction == 1:
                if y == y_max:
                    direction = 2
                    y_max -= 1
                    x -= 1
                else:
                    y += 1
            elif direction == 2:
                if x == x_min:
                    direction = 3
                    x_min += 1
                    y -= 1
                else:
                    x -= 1
            else:
                if y == y_min:
                    direction = 0
                    y_min += 1
                    x += 1
                else:
                    y -= 1
            count += 1
        return res


class Solution2:
    """
    Add by layer
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1
            if not left < right or not top < bottom:
                break
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][col])
            bottom -= 1
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
        return result


class Solution3:
    """
    Pop and rotate
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            matrix = (list(zip(*matrix)))[::-1]
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "spiralOrder",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert solution(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    assert solution(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    assert solution(matrix) == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]
