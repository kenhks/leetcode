from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for counter
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def divideArray(self, nums: List[int]) -> bool:
        return all(freq % 2 == 0 for freq in Counter(nums).values())


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "divideArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[3, 2, 3, 2, 2, 2])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(nums=[1, 2, 3, 4])
