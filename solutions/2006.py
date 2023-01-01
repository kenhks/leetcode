from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap with sorted keys
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for i in sorted(counter.keys()):
            if (i + k) in counter:
                ans += counter[i] * counter[i + k]
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countKDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 2, 1], k=1) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 3], k=3) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[3, 2, 1, 5, 4], k=2) == 3
