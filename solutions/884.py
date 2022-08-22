from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in Counter
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    m, n =  the length of string s1, s2
    """

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [
            word
            for word, count in Counter(s1.split() + s2.split()).items()
            if count == 1
        ]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "uncommonFromSentences",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("this apple is sweet", "this apple is sour")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("apple apple")
