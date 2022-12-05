from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    m = the number of col, n = the number of row
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        m, n = len(grid[0]), len(grid)

        def get_area(x, y):
            if y < 0 or x < 0 or x == m or y == n or (x, y) in seen or grid[y][x] == 0:
                return 0
            seen.add((x, y))
            return 1 + get_area(x, y + 1) + get_area(x, y - 1) + get_area(x - 1, y) + +get_area(x + 1, y)

        for y in range(n):
            for x in range(m):
                if (x, y) not in seen:
                    area = get_area(x, y)
                    ans = max(ans, area)
        return ans


class Solution2:
    """
    DFS, Iterative
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    m = the number of col, n = the number of row
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        m, n = len(grid[0]), len(grid)
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1 and (x, y) not in seen:
                    area = 1
                    ans = max(ans, area)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxAreaOfIsland",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert solution(grid) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert solution(grid) == 0
