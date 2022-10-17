from collections import Counter

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap to store frequency
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def areOccurrencesEqual(self, s: str) -> bool:
        freqs = list(Counter(s).values())
        return all(i == freqs[0] for i in freqs[1:])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "areOccurrencesEqual",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abacbc")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("aaabb")
