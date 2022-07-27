import pytest

from utils import parametrize_solution_cls


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_brackets = ["}", "]", ")"]
        open_brackets = ["{", "[", "("]
        bracket_map = {i: j for i, j in zip(close_brackets, open_brackets)}
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
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
