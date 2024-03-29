import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Convert to base 26
    Time Complexity: O(log(26, n)) = 2log(26, n)
    Space Complexity: O(log(26, n))
    """

    def convertToTitle(self, columnNumber: int) -> str:
        col_str = ""
        while columnNumber > 0:
            columnNumber, d = divmod(columnNumber - 1, 26)
            col_str = chr(d + 65) + col_str
        return col_str


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "convertToTitle",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1) == "A"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(28) == "AB"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(701) == "ZY"
