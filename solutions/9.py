import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Convert to string
    Time Complexity: O(log(10, n)) = 3log(10, n)
    Space Complexity: O(1)
    """

    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])


class Solution2:
    """
    Find digit value and use two pointer to check palidrome
    Time Complexity: O(log(10, n)) = 2log(10, n)
    Space Complexity: O(1)
    """

    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            digits = []
            while x > 0:
                x, right = divmod(x, 10)
                digits.append(right)
            left, right = 0, len(digits) - 1
            while left < right:
                if digits[left] != digits[right]:
                    return False
                left += 1
                right -= 1
            return True


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(121)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(-121)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(10)
