import math
from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_group = defaultdict(int)
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            dominoes_group[a, b] += 1
        ans = 0
        for count in dominoes_group.values():
            if count > 1:
                ans += math.comb(count, 2)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numEquivDominoPairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    assert solution(dominoes) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    assert solution(dominoes) == 3
