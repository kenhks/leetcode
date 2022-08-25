import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            mid_square = mid * mid
            if mid_square <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid_square < x:
                l = mid + 1
            elif mid_square > x:
                r = mid - 1
        return r


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "mySqrt",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(4) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(8) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(0) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(80) == 8


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution(12345) == 111
