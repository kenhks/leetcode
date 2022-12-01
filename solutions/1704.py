import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with two pointer
    Time Complexity: O(n)
    Space Complexity: O(1) = 10
    """

    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        a_vowel_count = b_vowel_count = 0
        i, j = 0, len(s) // 2
        while j < len(s):
            if s[i] in vowels:
                a_vowel_count += 1
            if s[j] in vowels:
                b_vowel_count += 1
            i += 1
            j += 1
        return a_vowel_count == b_vowel_count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "halvesAreAlike",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="book")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(s="textbook")
