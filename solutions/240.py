from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary Search by row
    Time Complexity: O(nlog(2, m))
    Space Complexity: O(1)
    n = the number of row in matrix
    m = the number of column in matrix
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        for row in matrix:
            if row[0] == target or row[-1] == target:
                ans = True
            elif row[0] < target < row[-1]:
                left, right = 1, len(row) - 2
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        ans = True
                        break
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            if ans:
                break
        return ans


class Solution2:
    """
    Binary Search by col
    Time Complexity: O(nlog(2, m))
    Space Complexity: O(1)
    n = the number of row in matrix
    m = the number of column in matrix
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        for col in zip(*matrix):
            if col[0] == target or col[-1] == target:
                ans = True
            elif col[0] < target < col[-1]:
                left, right = 1, len(col) - 2
                while left <= right:
                    mid = (left + right) // 2
                    if col[mid] == target:
                        ans = True
                        break
                    elif col[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            if ans:
                break
        return ans


class Solution3:
    """
    Matrix Traversal
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    n = the number of row in matrix
    m = the number of column in matrix
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        m, n = len(matrix[0]), len(matrix)
        x, y = m - 1, 0
        while x >= 0 and y < n:
            value = matrix[y][x]
            if value == target:
                ans = True
                break
            elif value > target:
                x -= 1
            else:
                y += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "searchMatrix",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert solution(matrix, target=5)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert not solution(matrix, target=20)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert solution(matrix, target=26)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    matrix = [
        [1, 1],
    ]
    assert not solution(matrix, target=2)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
    ]
    assert solution(matrix, target=12)
