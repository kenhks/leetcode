import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    min_value, max_value = -2147483648, 2147483647

    def myAtoi(self, s: str) -> int:
        left = right = -1
        for i, c in enumerate(s):
            if c == " " and (i == 0 or s[i - 1] == " "):
                continue
            elif c == "+" or c == "-":
                if left < 0:
                    left = i
                else:
                    break
            elif c.isdigit():
                if left < 0:
                    left = i
                right = i
            else:
                break
        ans = 0
        if 0 <= left <= right:
            ans = min(self.max_value, max(self.min_value, int(s[left : right + 1])))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "myAtoi",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("42") == 42


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("   -42") == -42


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("4193 with words") == 4193


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("+42-5") == 42


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("+-42") == 0


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution("3.14159") == 3


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution("words and 987") == 0


@pytest.mark.parametrize("solution", solutions)
def test_8(solution):
    assert solution("   +4 123") == 4
