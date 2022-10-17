from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap to store frequency
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        unique = True
        for i in Counter(arr).values():
            if i in seen:
                unique = False
                break
            seen.add(i)
        return unique


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "uniqueOccurrences",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 2, 1, 1, 3])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([1, 2])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
