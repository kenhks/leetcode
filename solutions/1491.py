from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = 1_000_000, 1000
        total = 0
        for i in salary:
            if i < min_salary:
                min_salary = i
            if i > max_salary:
                max_salary = i
            total += i
        return (total - min_salary - max_salary) / (len(salary) - 2)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "average",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([4000, 3000, 1000, 2000]) == 2500


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1000, 2000, 3000]) == 2000


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1000, 1000, 3000]) == 1000
