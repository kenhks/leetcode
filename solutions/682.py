from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(0, len(operations)):
            if operations[i][0] == "-" or operations[i].isdigit():
                scores.append(int(operations[i]))
            elif operations[i] == "D":
                scores.append(scores[-1] * 2)
            elif operations[i] == "C":
                scores.pop()
            elif operations[i] == "+":
                scores.append(scores[-1] + scores[-2])
        return sum(scores)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "calPoints",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["5", "2", "C", "D", "+"]) == 30


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["1", "C"]) == 0
