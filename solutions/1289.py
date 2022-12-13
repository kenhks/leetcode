from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^n) = n (n - 1) ^ n
    Space Complexity: O(n^n) = n (n - 1) ^ n
    n = len(matrix)
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 100 * n

        def dfs(row, col, prev):
            nonlocal ans
            print(f"{row, col = }")
            if 0 <= row < n and 0 <= col < n:
                prev += grid[row][col]
                for i in range(n):
                    if i == col:
                        continue
                    dfs(row + 1, i, prev)
            elif row == n:
                ans = min(prev, ans)

        if len(grid) == 1:
            ans = min(grid[0])
        else:
            for x in range(len(grid)):
                dfs(0, x, 0)
        return ans


class Solution2:
    """
    BFS, backtracking
    Time Complexity: O(n^2) = n^2
    Space Complexity: O(1)
    n = len(matrix)
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for row in range(1, n):
            for col in range(n):
                grid[row][col] += min(grid[row - 1][:col] + grid[row - 1][col + 1 :])
        return min(grid[-1])


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minFallingPathSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert solution(grid) == 13


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([[7]]) == 7
