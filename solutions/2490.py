import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Split to words
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        return all(prev[-1] == curr[0] for prev, curr in zip(words, words[1:] + [words[0]]))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isCircularSentence",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("leetcode exercises sound delightful")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("eetcode")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution("Leetcode is cool")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("abcd")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution("Leetcode eisc cool")
