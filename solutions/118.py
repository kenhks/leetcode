from functools import cache
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursion
    Time Complexity: O(n)
    Space Complexity: O(n(n+1)/2)
    """

    @cache
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            prev = self.generate(numRows - 1)
            prev.append([1] + [i + j for i, j in zip(prev[-1], prev[-1][1:])] + [1])
            return prev


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(n(n+1)/2)
    """

    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * i for i in range(1, numRows + 1)]
        for y in range(2, numRows):
            for i in range(1, len(result[y]) - 1):
                result[y][i] = result[y - 1][i - 1] + result[y - 1][i]
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "generate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(1) == [[1]]
