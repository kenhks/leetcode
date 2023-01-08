from collections import deque
from itertools import combinations
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n*n!)
    Space Complexity: O(1)
    """

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans, max_sum = None, float("-inf")
        for comb in combinations(nums, k):
            c_sum = sum(comb)
            if sum(comb) > max_sum:
                ans = comb
                max_sum = c_sum
        return list(ans)


class Solution2:
    """
    Sort with index and values
    Time Complexity: O(nlog(2, n)) = nlog(2, n)
    Space Complexity: O(n)
    """

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pairs = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))[-k:]
        pairs.sort(key=lambda x: x[0])
        return [i for _, i in pairs]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maxSubsequence",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[2, 1, 3, 3], k=2) == [3, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[-1, -2, 3, 4], k=3) == [-1, 3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    actual = solution(nums=[3, 4, 3, 3], k=2)
    assert actual == [3, 4] or actual == [4, 3]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(nums=[50, -75], k=2) == [50, -75]


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(nums=[9, -2, -1, -30, -40, 8, 5, 6, 7], k=3) == [9, 8, 7]
