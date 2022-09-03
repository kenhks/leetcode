from collections import Counter
from heapq import nsmallest
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with hashmap counter
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(n)
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return [i[0] for i in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:k]]


class Solution2:
    """
    Scan with hashmap counter, heapify with max heap
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(n)
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return nsmallest(k, c.keys(), key=lambda x: (-c[x], x))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "topKFrequent",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    assert solution(words, k=2) == ["i", "love"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    assert solution(words, k=4) == ["the", "is", "sunny", "day"]
