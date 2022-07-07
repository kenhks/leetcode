import pytest

from utils import parametrize_solution_cls


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = [i for i in s.lower() if i.isalnum()]
        left, right = 0, len(valid_chars) - 1
        while left <= right:
            if valid_chars[left] != valid_chars[right]:
                return False
            left += 1
            right -= 1
        return True


solutions = parametrize_solution_cls(
    [
        Solution,
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
