from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two hashmap to store frequency
    Time Complexity: O(m + n) = 2m + n
    Space Complexity: O(m + n)
    m, n = len(words1), len(words2)
    """

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1_counter = Counter(words1)
        w2_counter = Counter(words2)
        ans = 0
        for w in w1_counter:
            if w1_counter[w] == 1 and w2_counter.get(w, 0) == 1:
                ans += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countWords",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    words1 = ["leetcode", "is", "amazing", "as", "is"]
    words2 = ["amazing", "leetcode", "is"]
    assert solution(words1, words2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    words1 = ["b", "bb", "bbb"]
    words2 = ["a", "aa", "aaa"]
    assert solution(words1, words2) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    words1 = ["a", "ab"]
    words2 = ["a", "a", "a", "ab"]
    assert solution(words1, words2) == 1
