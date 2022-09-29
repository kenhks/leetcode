from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap to store modulo count
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modulo_count = {}
        count = 0
        for t in time:
            t %= 60
            count += modulo_count.get(60 - t, 0)
            if t == 0:
                count += modulo_count.get(0, 0)
            modulo_count[t] = modulo_count.get(t, 0) + 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numPairsDivisibleBy60",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    time = [30, 20, 150, 100, 40]
    assert solution(time) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    time = [60, 60, 60]
    assert solution(time) == 3
