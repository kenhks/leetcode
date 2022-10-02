import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(log(10, n))
    Space Complexity: O(1)
    """

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n /= p
        return n == 1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isUgly",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(6)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(1)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(14)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(-5)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(8)
