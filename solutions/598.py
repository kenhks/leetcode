from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(mn * p)
    Space Complexity: O(max(m, n))
    p = len(ops)
    """

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            ans = m * n
        else:
            matrix = [[0 for _ in range(m)] for _ in range(n)]
            for a, b in ops:
                for y in range(b):
                    for x in range(a):
                        matrix[y][x] += 1
            counter = {}
            for row in matrix:
                for e in row:
                    counter[e] = counter.get(e, 0) + 1
            ans = counter[max(counter.keys())]
        return ans


class Solution2:
    """
    Check minimum
    Time Complexity: O(p)
    Space Complexity: O(1)
    p = len(ops)
    """

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m, min_n = m, n
        for a, b in ops:
            min_m = min(a, min_m)
            min_n = min(b, min_n)
        return min_m * min_n


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maxCount",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    m, n = 3, 3
    ops = [[2, 2], [3, 3]]
    assert solution(m, n, ops) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    m, n = 3, 3
    ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
    assert solution(m, n, ops) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    m, n = 3, 3
    ops = []
    assert solution(m, n, ops) == 9
