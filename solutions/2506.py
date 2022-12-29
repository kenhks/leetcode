from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for similar group size
    Time Complexity: O(m) = 3n
    Space Complexity: O(n)
    m = length of total characters
    n = length of words
    """

    def similarPairs(self, words: List[str]) -> int:
        count = 0
        chars_group = {}
        for word in words:
            word_chars = "".join(sorted(set(word)))
            prev_size = chars_group.get(word_chars, 0)
            count += prev_size
            chars_group[word_chars] = prev_size + 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "similarPairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(words=["aba", "aabb", "abcd", "bac", "aabc"]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(words=["aabb", "ab", "ba"]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(words=["nba", "cba", "dba"]) == 0
