import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2 :])
        return s


class Solution2:
    """
    Iterative, use stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "makeGood",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("leEeetcode") == "leetcode"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("abBAcC") == ""


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("s") == "s"
