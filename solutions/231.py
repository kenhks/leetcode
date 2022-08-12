import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Count number of 1 in binary
    Time Complexity: O(log(n)) = log(2, n)
    Space Complexity: O(1)
    """

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and "{:b}".format(n).count("1") == 1


class Solution2:
    """
    Bitwise operation
    Time Complexity: O(1) = 2
    Space Complexity: O(1)
    """

    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isPowerOfTwo",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(2)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(1)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(8)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(-8)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution(3)


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert not solution(17)
