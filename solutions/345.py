import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two Pointers
    Time Complexity: O(n) = n
    Space Complexity: O(n) = n
    """

    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in self.vowels:
                left += 1
            if s[right] not in self.vowels:
                right -= 1
            if s[left] in self.vowels and s[right] in self.vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "reverseVowels",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("hello") == "holle"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("leetcode") == "leotcede"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("abc") == "abc"
