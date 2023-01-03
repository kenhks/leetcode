from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    6 Pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for i in range(n)]
        x, y = 0, 0
        min_x = min_y = 0
        max_x = max_y = n - 1
        for i in range(1, n * n + 1):
            ans[y][x] = i
            if x < max_x and y == min_y:
                x += 1
                if x == max_x:
                    min_y += 1
            elif x == max_x and y < max_y:
                y += 1
                if y == max_y:
                    max_x -= 1
            elif x > min_x and y == max_y:
                x -= 1
                if x == min_x:
                    max_y -= 1
            elif x == min_x and y > min_y:
                y -= 1
                if y == min_y:
                    min_x += 1
        return ans


class Solution2:
    """
    4 Pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for i in range(n)]
        y, x, dy, dx = 0, 0, 0, 1
        for k in range(1, n * n + 1):
            ans[y][x] = k
            if ans[(y + dy) % n][(x + dx) % n]:
                dy, dx = dx, -dy
            y += dy
            x += dx
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "generateMatrix",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
    assert solution(n=3) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [[1]]
    assert solution(n=1) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    expected = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]
    assert solution(n=5) == expected
