import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity:
    Space Complexity:
    """

    def myfuncname(self):
        pass


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "myfuncname",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution()


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution()


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution()
