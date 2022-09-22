from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DP Bottom-up
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        path = {(0, 0): 1}
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        for y in range(n):
            for x in range(m):
                if obstacleGrid[y][x] == 1:
                    path[x, y] = 0
                else:
                    if x == 0 and y == 0:
                        pass
                    elif x == 0 and y > 0:
                        if obstacleGrid[y - 1][x] == 1:
                            path[x, y] = 0
                        else:
                            path[x, y] = path[x, y - 1]
                    elif y == 0 and x > 0:
                        if obstacleGrid[y][x - 1] == 1:
                            path[x, y] = 0
                        else:
                            path[x, y] = path[x - 1, y]
                    else:
                        path[x, y] = path[x - 1, y] + path[x, y - 1]
        return path[m - 1, n - 1]


class Solution2:
    """
    DP Bottom-up, modify input
    Time Complexity: O(mn)
    Space Complexity: O(1)
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        for x in range(1, m):
            obstacleGrid[0][x] = int(obstacleGrid[0][x] == 0 and obstacleGrid[0][x - 1] == 1)
        for y in range(1, n):
            obstacleGrid[y][0] = int(obstacleGrid[y][0] == 0 and obstacleGrid[y - 1][0] == 1)

        for y in range(1, n):
            for x in range(1, m):
                if obstacleGrid[y][x] == 0:
                    obstacleGrid[y][x] = obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]
                else:
                    obstacleGrid[y][x] = 0
        return obstacleGrid[n - 1][m - 1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "uniquePathsWithObstacles",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert solution(obstacleGrid) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    obstacleGrid = [
        [0, 1],
        [0, 0],
    ]
    assert solution(obstacleGrid) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    obstacleGrid = [
        [1],
    ]
    assert solution(obstacleGrid) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    obstacleGrid = [
        [0, 1],
        [1, 0],
    ]
    assert solution(obstacleGrid) == 0
