from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n*3^n) = n * 3 ^ (n - 1)
    Space Complexity: O(n*3^n) = n * 3 ^ (n - 1)
    n = len(matrix)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ans = 100 * n

        def dfs(row, col, prev):
            nonlocal ans
            if 0 <= row < n and 0 <= col < n:
                prev += matrix[row][col]
                dfs(row + 1, col - 1, prev)
                dfs(row + 1, col, prev)
                dfs(row + 1, col + 1, prev)
            elif row == n:
                ans = min(prev, ans)

        for x in range(len(matrix)):
            dfs(0, x, 0)
        return ans


class Solution2:
    """
    BFS, backtracking
    Time Complexity: O(n^2) = 3n^2
    Space Complexity: O(1)
    n = len(matrix)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                matrix[row][col] += min(matrix[row - 1][max(0, col - 1) : col + 2])
        return min(matrix[-1])


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minFallingPathSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([[-19, 57], [-40, -5]]) == -59


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([[1]]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([[82, 81], [69, 33]]) == 114
