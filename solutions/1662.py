from itertools import zip_longest
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Concat string
    Time Complexity: O(min(m, n))
    Space Complexity: O(m + n)
    m = the number of characters in word1
    n = the number of characters in word2
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


class Solution2:
    """
    Compare character one by one with generator
    Time Complexity: O(min(m, n))
    Space Complexity: O(m + n)
    m = the number of characters in word1
    n = the number of characters in word2
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def flatten(words):
            for w in words:
                for c in w:
                    yield c

        ans = True
        for i, j in zip_longest(flatten(word1), flatten(word2)):
            if i != j:
                ans = False
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "arrayStringsAreEqual",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(word1=["ab", "c"], word2=["a", "bc"])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(word1=["a", "cb"], word2=["ab", "c"])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(word1=["abc", "d", "defg"], word2=["abcddefg"])
