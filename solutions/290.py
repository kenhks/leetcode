import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check the pattern hashmap is bijective
    Time Complexity: O(s)
    Space Complexity: O(1) = 52
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(s) != len(pattern):
            return False
        same_pattern: bool = True
        p_word_lookup = {}
        word_p_lookup = {}
        for p, word in zip(pattern, words):
            if p not in p_word_lookup:
                p_word_lookup[p] = word
            elif p_word_lookup[p] != word:
                same_pattern = False
                break
            if word not in word_p_lookup:
                word_p_lookup[word] = p
            elif word_p_lookup[word] != p:
                same_pattern = False
                break
        return same_pattern


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "wordPattern",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(pattern="abba", s="dog cat cat dog")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(pattern="abba", s="dog cat cat fish")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(pattern="aaaa", s="dog cat cat dog")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(pattern="aaa", s="aa aa aa aa")
