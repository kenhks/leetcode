from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        if income > 0 and brackets:
            prev_upper = 0
            i = 0
            while income > 0 and i < len(brackets):
                upper, percent = brackets[i]
                income_diff = min(upper - prev_upper, income)
                tax += (income_diff) * percent / 100
                income -= income_diff
                prev_upper = upper
                i += 1
        return tax


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "calculateTax",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(brackets=[[3, 50], [7, 10], [12, 25]], income=10) == 2.65


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(brackets=[[1, 0], [4, 25], [5, 50]], income=2) == 0.25


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(brackets=[[2, 50]], income=0) == 0
