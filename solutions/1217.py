from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for odd and even count
    Time Complexity: O(n)
    Space Complexity: O(1) = 2
    """

    def minCostToMoveChips(self, position: List[int]) -> int:
        count = defaultdict(int)
        for p in position:
            count[p % 2] += 1
        return min(count.values()) if len(count) == 2 else 0


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minCostToMoveChips",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(position=[1, 2, 3]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(position=[2, 2, 2, 3, 3]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(position=[1, 1000000000]) == 1
