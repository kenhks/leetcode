import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for c in s[1:]:
            if len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "removeDuplicates",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abbaca") == "ca"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("azxxzy") == "ay"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("a") == "a"
