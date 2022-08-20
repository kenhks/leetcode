from re import T
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in
    Time Complexity: O(n)
    Space Complexity: O(k)
    n = length of input string s
    k = the number of word in s
    """

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


class Solution2:
    """
    Scan with word check
    Time Complexity: O(n)
    Space Complexity: O(1)
    n = length of input string s
    """

    def lengthOfLastWord(self, s: str) -> int:
        size = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char != " ":
                size += 1
            elif size > 0:
                break
        return size


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "lengthOfLastWord",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("Hello World") == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("   fly me   to   the moon  ") == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("luffy is still joyboy") == 6
