import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


class Solution2:
    """
    Bitwise Modulo
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def canWinNim(self, n: int) -> bool:
        return (n & 3) != 0


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "canWinNim",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(2)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(4)
