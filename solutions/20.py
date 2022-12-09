import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in bracket_map:
                stack.append(c)
            elif len(stack) == 0 or bracket_map[stack.pop()] != c:
                stack.append(c)
                break
        return len(stack) == 0


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isValid",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("()")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("()[]{}")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution("(]")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("]")
