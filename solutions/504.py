import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(log(7, n))
    Space Complexity: O(1)
    """

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            return "-" + self.convertToBase7(-num)
        ans = ""
        while num > 0:
            num, digit = divmod(num, 7)
            ans = str(digit) + ans
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "convertToBase7",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(100) == "202"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(-7) == "-10"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(0) == "0"
