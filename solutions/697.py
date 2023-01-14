from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    3 Hashmap
    Time Complexity: O(n) = 4n
    Space Complexity: O(n)
    """

    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 1
        counter = defaultdict(int)
        first_occur, last_occur = {}, {}
        for i, n in enumerate(nums):
            counter[n] += 1
            if n not in first_occur:
                first_occur[n] = i
            last_occur[n] = i
            degree = max(degree, counter[n])
        ans = len(nums)
        for n, freq in counter.items():
            if freq == degree:
                ans = min(ans, last_occur[n] - first_occur[n] + 1)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findShortestSubArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 2, 3, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 2, 2, 3, 1, 4, 2]) == 6
