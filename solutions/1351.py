from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0]) - 1, -1, -1):
                if grid[y][x] < 0:
                    count += 1
                else:
                    break
        return count


class Solution2:
    """
    Binary Search on row
    Time Complexity: O(m log(2, n))
    Space Complexity: O(1)
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            if row[0] < 0:
                count += len(row)
            elif row[-1] >= 0:
                continue
            else:
                left, right = 0, len(row) - 1
                while left < right:
                    mid = (left + right) // 2
                    if row[mid] >= 0:
                        left = mid + 1
                    else:
                        right = mid
                count += len(row) - left
        return count


class Solution3:
    """
    Matrix Traversal
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        count = 0
        row, col = 0, m - 1
        while row < n and 0 <= col:
            while col >= 0:
                if grid[row][col] < 0:
                    count += n - row
                    col -= 1
                else:
                    row += 1
                    break
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "countNegatives",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    mat = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3],
    ]
    assert solution(mat) == 8


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    mat = [
        [3, 2],
        [1, 0],
    ]
    assert solution(mat) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    mat = [
        [-1, -3],
        [-2, -4],
    ]
    assert solution(mat) == 4


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    mat = [
        [3, 2, 1],
        [1, 1, 1],
        [0, 0, 0],
        [-1, -6, -7],
        [-3, -6, -7],
        [-5, -6, -7],
    ]
    assert solution(mat) == 9
