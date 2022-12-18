from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Stacks
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stacks = [int(tokens[0])]
        for i in tokens[1:]:
            if i == "+":
                b, a = stacks.pop(), stacks.pop()
                new_value = a + b
            elif i == "-":
                b, a = stacks.pop(), stacks.pop()
                new_value = a - b
            elif i == "*":
                b, a = stacks.pop(), stacks.pop()
                new_value = a * b
            elif i == "/":
                b, a = stacks.pop(), stacks.pop()
                new_value = int(a / b)
            else:
                new_value = int(i)
            stacks.append(new_value)
        return stacks[-1]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "evalRPN",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["2", "1", "+", "3", "*"]) == 9


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["4", "13", "5", "/", "+"]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(["10"]) == 10
