import heapq
from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use Counter
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


class Solution2:
    """
    Use Heapq
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        return [x[1] for x in heapq.nlargest(k, [(j, i) for i, j in freq.items()])]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "topKFrequent",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 1, 1, 2, 2, 3], 2) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1], 1) == [1]
