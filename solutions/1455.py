import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Split and scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = -1
        for i, w in enumerate(sentence.split(), start=1):
            if w[: len(searchWord)] == searchWord:
                ans = i
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isPrefixOfWord",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    sentence = "i love eating burger"
    searchWord = "burg"
    assert solution(sentence, searchWord) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    sentence = "this problem is an easy problem"
    searchWord = "pro"
    assert solution(sentence, searchWord) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    sentence = "i am tired"
    searchWord = "you"
    assert solution(sentence, searchWord) == -1
