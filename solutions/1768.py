from io import StringIO
from itertools import zip_longest

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Concat alternatively
    Time Complexity: O(m+n)
    Space Complexity: O(1)
    m = len(word1), n = len(word2)
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i, j in zip(word1, word2):
            ans += f"{i}{j}"
        if len(word2) > len(word1):
            ans += word2[len(word1) - len(word2) :]
        elif len(word1) > len(word2):
            ans += word1[len(word2) - len(word1) :]
        return ans


class Solution2:
    """
    Concat alternatively
    Time Complexity: O(m+n)
    Space Complexity: O(1)
    m = len(word1), n = len(word2)
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = StringIO()
        for i, j in zip_longest(word1, word2):
            if i:
                ans.write(i)
            if j:
                ans.write(j)
        return ans.getvalue()


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "mergeAlternately",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abc", "pqr") == "apbqcr"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("ab", "pqrs") == "apbqrs"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("abcd", "pq") == "apbqcd"
