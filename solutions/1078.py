from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Split and scan
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        ans = []
        for i in range(0, len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findOcurrences",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    assert solution(text, first, second) == ["girl", "student"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    text = "we will we will rock you"
    first = "we"
    second = "will"
    assert solution(text, first, second) == ["we", "rock"]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    text = "we will we will rock you"
    first = "we2"
    second = "will3"
    assert solution(text, first, second) == []
