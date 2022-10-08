from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use counter hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        count = {}
        for n in nums:
            if n in count:
                good_pairs += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return good_pairs


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numIdenticalPairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3, 1, 1, 3]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1, 1, 1]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 2, 3]) == 0
