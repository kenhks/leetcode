import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check with two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = n
    """

    def isPalindrome(self, s: str) -> bool:
        valid_chars = [i for i in s.lower() if i.isalnum()]
        left, right = 0, len(valid_chars) - 1
        while left < right:
            if valid_chars[left] != valid_chars[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    """
    Check with two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = 2n
    """

    def isPalindrome(self, s: str) -> bool:
        valid_chars = [i for i in s.lower() if i.isalnum()]
        return valid_chars == valid_chars[::-1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("A man, a plan, a canal: Panama")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("race a car")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(" ")
