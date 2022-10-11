import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    3 Case Approach
    CASE 1: single letter string
    CASE 2: replace first non 'a' character with first half of palidrome
    CASE 3: string are all 'a' and replace last character with 'b'
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        left, right = 0, len(palindrome) - 1
        while left < right:
            if palindrome[left] != "a":
                ans = palindrome[:left] + "a" + palindrome[left + 1 :]
                break
            left += 1
            right -= 1
        else:
            ans = palindrome[:-1] + "b"
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "breakPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abccba") == "aaccba"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("a") == ""


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("aa") == "ab"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("aaaaaa") == "aaaaab"


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("aabbaa") == "aaabaa"
