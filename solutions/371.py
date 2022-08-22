import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Bitwise Manipluation
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > 0 else a


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "getSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1, 2) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(2, 3) == 5


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(-1, -6) == -7


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(-1, 1) == 0
