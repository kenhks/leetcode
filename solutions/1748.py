from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two Hashset
    Time Complexity: O(n)
    Space Complexity: O(n) = 2n
    """

    def sumOfUnique(self, nums: List[int]) -> int:
        seen = set()
        duplicate = set()
        for n in nums:
            if n in seen:
                duplicate.add(n)
            seen.add(n)
        return sum(seen) - sum(duplicate)


class Solution2:
    """
    Hashmap
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(i for i, j in Counter(nums).items() if j == 1)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "sumOfUnique",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3, 2]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 1, 1, 1, 1]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[1, 2, 3, 4, 5]) == 15
