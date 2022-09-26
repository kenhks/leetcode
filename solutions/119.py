from functools import cache
from math import comb
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursion
    Time Complexity: O(n)
    Space Complexity: O(n^2) = n(n+1)/2
    """

    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def generate(row: int):
            if row == 0:
                return [[1]]
            else:
                prev = generate(row - 1)
                prev.append([1] + [i + j for i, j in zip(prev[-1], prev[-1][1:])] + [1])
                return prev

        return generate(rowIndex)[-1]


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for _ in range(rowIndex):
            result = [1] + [i + j for i, j in zip(result, result[1:])] + [1]
        return result


class Solution3:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "getRow",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(3) == [1, 3, 3, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(0) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1) == [1, 1]
