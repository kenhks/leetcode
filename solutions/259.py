import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(log(10, n))
    Space Complexity: O(1)
    """

    def addDigits(self, num: int) -> int:
        while num > 9:
            new_num = 0
            while num > 0:
                num, digit = divmod(num, 10)
                new_num += digit
            num = new_num
        return num


class Solution2:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 10:
            return num
        else:
            return num % 9


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "addDigits",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(38) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(0) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1234) == 1
