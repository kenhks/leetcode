import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Reverse as string
    Time Complexity: O(log(10, x))
    Space Complexity: O(1)
    """

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            if x > 0:
                reversed_x = int(str(x)[::-1])
            else:
                reversed_x = -int(str(-x)[::-1])
            if -(2**31) <= reversed_x <= 2**31 - 1:
                return reversed_x
            else:
                return 0


class Solution2:
    """
    Pop right most digit with modulo
    Time Complexity: O(log(10, x))
    Space Complexity: O(1)
    """

    def reverse(self, x: int) -> int:
        MAX_OVERFLOW = 2147483647  # 2^31 - 1
        rev = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
            MAX_OVERFLOW += 1
        while x != 0:
            x, rightmost_digit = divmod(x, 10)
            rev = rev * 10 + rightmost_digit
        if rev > MAX_OVERFLOW:
            return 0
        else:
            return sign * rev


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "reverse",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(123) == 321


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(-123) == -321


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(120) == 21


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(1534236469) == 0
