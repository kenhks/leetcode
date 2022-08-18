import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DP Bottom-up
    Time Complexity: O(mn) = mn - n - m + 1
    Space Complexity: O(mn) = (m - 1) * (n - 1) + 1
    """

    def uniquePaths(self, m: int, n: int) -> int:
        path = {(0, 0): 1}
        if m == 1 or n == 1:
            return 1
        for y in range(1, m):
            for x in range(1, n):
                if x == 1:
                    path[x, y] = path.get((x, y - 1), 1) + 1
                elif y == 1:
                    path[x, y] = path.get((x - 1, y), 1) + 1
                else:
                    path[x, y] = path[x - 1, y] + path[x, y - 1]
        return path[n - 1, m - 1]


class Solution2:
    """
    Math
    Time Complexity: O(mn) = mn - 2 + m - 1 + n - 1
    Space Complexity: O(1)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return int(
            math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)
        )


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "uniquePaths",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(3, 7) == 28


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(3, 2) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1, 2) == 1
